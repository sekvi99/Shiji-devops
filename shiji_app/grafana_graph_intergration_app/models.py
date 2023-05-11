from django.db import models

class EurCurrencyModel(models.Model):
    """
    ORM Model for Euro currency rate.
    
    Args:
        models (_type_): Inheritence of models.Model for propper ORM implementation.
    """
    id = models.AutoField(primary_key=True) # Primary key
    date = models.DateField(blank=True, null=True)
    eur = models.FloatField(blank=True, null=True)
    
    def __str__(self) -> str:
        """
        Overriden method __str__ for propper admin object instance representation.

        Returns:
            str: String representation of object in admin panel.
        """
        return f'Euro: {self.eur} for Date: {self.date}'
    
    class Meta:
        """
        Meta data for Euro ORM.
        """
        ordering = ['date']
        
class USDCurrencyModel(models.Model):
    """
    ORM Model for USD currency rate.
    
    Args:
        models (_type_): Inheritence of models.Model for propper ORM implementation.
    """
    id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    usd = models.FloatField(blank=True, null=True)
    
    def __str__(self) -> str:
        """
        Overriden method __str__ for propper admin object instance representation.

        Returns:
            str: String representation of object in admin panel.
        """
        return f'USD: {self.usd} for Date: {self.date}'
    
    class Meta:
        """
        Meta data for USD ORM.
        """
        ordering = ['date']
    
class GBPCurrencyModel(models.Model):
    """
    ORM Model for GBP currency rate.
    
    Args:
        models (_type_): Inheritence of models.Model for propper ORM implementation.
    """
    id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    gbp = models.FloatField(blank=True, null=True)
    
    def __str__(self) -> str:
        """
        Overriden method __str__ for propper admin object instance representation.

        Returns:
            str: String representation of object in admin panel.
        """
        return f'GBP: {self.gbp} for Date: {self.date}'
    
    class Meta:
        """
        Meta data for GBP ORM.
        """
        ordering = ['date']
