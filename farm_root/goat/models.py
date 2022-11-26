from django.db import models
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Goat(models.Model):
    TEST_CHOICES = [
        ('POSITIVE', 'Positive'),
        ('NEGATIVE', 'Negative'),
        ('NOT', 'Not Tested'),
    ]

    STATUS_CHOICES = [
        ('RETIRED','Retired'),
        ('SOLD','Sold'),
        ('BREEDER','Breeder'),
        ('KID','Kid'),
    ]

    AVAIL_CHOICES = [
        ('YES', 'Available'),
        ('NO', 'Not Available'),
        ('PENDING', 'Pending'),
        ('SOON', 'Coming Soon')
    ]

    name = models.CharField(max_length=50, unique=True)
    dob = models.DateField()
    test_result = models.CharField(
        max_length=8,
        choices=TEST_CHOICES,
        default='NEGATIVE',)
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='KID',)
    availability = models.CharField(
        max_length=7,
        choices=AVAIL_CHOICES,
        default='NO',)
    price = models.IntegerField(default=0)
    comments = models.TextField(blank=True, null=True)
    sire = models.ForeignKey(
        'Buck',
        on_delete=models.PROTECT,
        related_name="sirekids",
        blank=True,
        null=True
    )
    dam = models.ForeignKey(
        'Doe',
        on_delete=models.PROTECT,
        related_name="damkids",
        blank=True,
        null=True
    )
    ss = models.ForeignKey(
        'Buck',
        on_delete=models.PROTECT,
        related_name="ssgrandkid",
        blank=True,
        null=True
    )
    sd = models.ForeignKey(
        'Doe',
        on_delete=models.PROTECT,
        related_name="sdgrandkid",
        blank=True,
        null=True
    )
    ds = models.ForeignKey(
        'Buck',
        on_delete=models.PROTECT,
        related_name="dsgrandkid",
        blank=True,
        null=True
    )
    dd = models.ForeignKey(
        'Doe',
        on_delete=models.PROTECT,
        related_name="ddgrandkid",
        blank=True,
        null=True
    )
    profile_pic = models.ImageField()
    profile_pic_thumbnail = ImageSpecField(
                                source='profile_pic',
                                processors=[ResizeToFill(300,225)],
                                format='JPEG',
                                options={'quality':60})
    profile_pic_regular = ImageSpecField(source='profile_pic',
                                   processors=[
                                    ResizeToFill(800, 600),
                                    ],
                                   format='JPEG',
                                   options={'quality': 60})
    profile_pic_medium = ImageSpecField(source='profile_pic',
                                      processors=[
                                      ResizeToFill(700 , 525),
                                      ],
                                      format='JPEG',
                                      options={'quality': 60})

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name

class Buck(Goat):
    GENDER_CHOICES = [
        ('BUCK', 'Buck'),
        ('WETHER', 'Wether')
    ]

    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default='BUCK',
    )

    def get_absolute_url(self):
        return reverse('goats:buck-detail', kwargs={'pk': self.pk})

class Doe(Goat):
    BRED_CHOICES = [
        ('BRED','Bred'),
        ('OPEN', 'Open')
    ]

    bred_status = models.CharField(
        max_length=4,
        choices=BRED_CHOICES,
        default='OPEN',
    )
    bred_to = models.ForeignKey(
        Buck,
        on_delete=models.PROTECT,
        related_name="mate",
        blank=True,
        null=True
    )
    due = models.DateField(
        verbose_name="estimated due date",
        blank=True,
        null=True
        )

    def get_absolute_url(self):
        return reverse('goats:doe-detail', kwargs={'pk': self.pk})

class Photo(models.Model):
    goat = models.ForeignKey(
        Goat,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(verbose_name="photo album", blank=True)
    image_thumbnail = ImageSpecField(
                                source='image',
                                processors=[ResizeToFill(300,225)],
                                format='JPEG',
                                options={'quality':60})
    image_regular = ImageSpecField(source='image',
                                   processors=[
                                    ResizeToFill(800, 600),
                                    ],
                                   format='JPEG',
                                   options={'quality': 60})
    image_medium = ImageSpecField(source='image',
                                      processors=[
                                      ResizeToFill(700 , 525),
                                      ],
                                      format='JPEG',
                                      options={'quality': 60})
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description
