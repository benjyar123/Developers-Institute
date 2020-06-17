from .models import Room

def populate_rooms():
        for x in range(2):
            Room.objects.create(beds=1, rate=50, category="Single", img_url="https://pix10.agoda.net/hotelImages/1030657/-1/88c38b77b84ff3ee5bede2c338438a5c.jpg?s=1024x768")
            Room.objects.create(beds=2, rate=80, category="Double",
                                img_url="https://pix10.agoda.net/hotelImages/123/1235585/1235585_17091311590056285210.jpg?s=1024x768")
            Room.objects.create(beds=3, rate=100, category="Family",
                                img_url="https://q-cf.bstatic.com/images/hotel/max1024x768/177/177196460.jpg")
            Room.objects.create(beds=4, rate=125, category="Family",
                                img_url="https://santorinidave.com/wp-content/uploads/2017/08/quadruple-room-for-family-of-four-stockholm.jpg")


