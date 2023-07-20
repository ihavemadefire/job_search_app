from django.db import models


class PersonOfContact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    DORR = [
        ('Direct', 'Direct'),
        ('Recruiter', 'Recruiter')
    ]
    direct_or_recruiter = models.CharField(choices=DORR, max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    company_name = models.CharField(max_length=60)
    person_of_contact = models.ForeignKey(PersonOfContact, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.company_name


class ContactEvent(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    event_date = models.DateField()
    person_of_contact = models.ForeignKey(PersonOfContact, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return f"{str(self.person_of_contact)} {self.event_date}"


class Application(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    industry = models.CharField(max_length=60)
    role_title = models.CharField(max_length=60, null=True, blank=True)
    job_description = models.CharField(max_length=120, null=True, blank=True)
    date_applied = models.DateField()
    contact_events = models.ForeignKey(ContactEvent, on_delete=models.CASCADE, null=True, blank=True)
    person_of_contact = models.ForeignKey(PersonOfContact, on_delete=models.CASCADE, null=True, blank=True)
    STATUSES = [
        ('Applied', 'Applied'),
        ('Active', 'Active'),
        ('Dead', 'Dead')
    ]
    status = models.CharField(
        choices=STATUSES,
        max_length=10
    )

    def __str__(self):
        return str(self.company_name)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    date = models.DateField
    body = models.TextField()
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return str(self.title)