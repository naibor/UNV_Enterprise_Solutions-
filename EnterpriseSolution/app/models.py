from django.db import models

    
class Office(models.Model):
    """
    implementation offices
    """
    implementation_office =models.CharField(max_length=100)
    # implementing_office_id

class Country(models.Model):
    """
    countries
    """
    country = models.CharField(max_length=100)
    # country_id
    
class Project(models.Model):
    """
    projects
    """
    project_ref = models.CharField(max_length=100)
    project_title = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    duration =  models.IntegerField(default=0)
    end_date = models.DateTimeField('end date')
    grant_amount = models.DecimalField(max_digits=6, decimal_places=2)
    first_disbursement_amount = models.DecimalField(max_digits=6, decimal_places=2)
    readiness_or_NAP =models.CharField(max_length=100)
    types_of_readiness = models.CharField(max_length=100)
    status = models.CharField(max_length=100,blank=True)


class ProjectImplementation(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT )
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT )
    implementing_office_id = models.ForeignKey(Office, on_delete=models.PROTECT)
    status = models.CharField(max_length=100)
 
