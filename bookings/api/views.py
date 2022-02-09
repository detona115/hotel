from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import timedelta, date, datetime
from django.core.exceptions import ValidationError, FieldError
from ..models import Booking
from accounts.models import CustomUser
from rooms.models import Room
from ..serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):

        data = request.data

        start_date = datetime.strptime(data["start_date"], '%Y-%m-%d').date()
        end_date = datetime.strptime(data["end_date"], '%Y-%m-%d').date()

        if start_date <= date.today():
            return Response({"message": "start_date must be greater than the current date."})
        if start_date > end_date:
            return Response({"message": "start_date can't be greater than end_date!"})
        if end_date - start_date > timedelta(3):
            return Response({"message": "You can't book a room for more than 3 days!"})
        if start_date - date.today() > timedelta(30):
            return Response({"message": "You can't book a room more than 30 days in advance!"})

        limit1 = datetime.strptime(data["start_date"], '%Y-%m-%d').date() - timedelta(3)
        limit2 = datetime.strptime(data["end_date"], '%Y-%m-%d').date() - timedelta(3)
        limit1, limit2 = str(limit1), str(limit2)

        start = Booking.objects.filter(start_date__range=(limit1, data["start_date"]))

        end = Booking.objects.filter(end_date__range=(limit2, data["end_date"]))
        print(start, end)
        if start:
            return Response(
                {"message": "The start_date chosen is already booked!"},
                status=status.HTTP_403_FORBIDDEN
            )
        if end:
            return Response(
                {"message": "The start_date is already booked!"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs['pk'])
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # data = request.data
        #
        # user = CustomUser.objects.get(id=data["user"])
        # room = Room.objects.get(id=data["room"])
        #
        # instance.user = user
        # instance.room = room
        # instance.start_date = data["start_date"]
        # instance.end_date = data["end_date"]
        #
        # instance.save()
        #
        # serializer = BookingSerializer(instance)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        pk = None
        try:
            if kwargs['pk'] and int(kwargs['pk']):
                pk = int(kwargs['pk'])
        except ValueError:
            return Response(
                {"message": "The parameter must be convertible to int!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        query = Booking.objects.filter(id=pk)
        if query:
            Booking.objects.filter(id=pk).delete()
            return Response(
                {"message": "Booking deleted successfully!"},
                status=status.HTTP_204_NO_CONTENT
            )

        return Response(
            {"message": "Booking not found!"},
            status=status.HTTP_404_NOT_FOUND
        )

