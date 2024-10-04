# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.TextField(db_column='CategoryName', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categories'


class Customercustomerdemo(models.Model):
    customerid = models.OneToOneField('Customers', models.DO_NOTHING, db_column='CustomerID', primary_key=True)  # Field name made lowercase. The composite primary key (CustomerID, CustomerTypeID) found, that is not supported. The first column is selected.
    customertypeid = models.ForeignKey('Customerdemographics', models.DO_NOTHING, db_column='CustomerTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerCustomerDemo'


class Customerdemographics(models.Model):
    customertypeid = models.TextField(db_column='CustomerTypeID', primary_key=True)  # Field name made lowercase.
    customerdesc = models.TextField(db_column='CustomerDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerDemographics'


class Customers(models.Model):
    customerid = models.TextField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
    contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
    contacttitle = models.TextField(db_column='ContactTitle', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Employeeterritories(models.Model):
    employeeid = models.OneToOneField('Employees', models.DO_NOTHING, db_column='EmployeeID', primary_key=True)  # Field name made lowercase. The composite primary key (EmployeeID, TerritoryID) found, that is not supported. The first column is selected.
    territoryid = models.ForeignKey('Territories', models.DO_NOTHING, db_column='TerritoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeTerritories'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    titleofcourtesy = models.TextField(db_column='TitleOfCourtesy', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    homephone = models.TextField(db_column='HomePhone', blank=True, null=True)  # Field name made lowercase.
    extension = models.TextField(db_column='Extension', blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='ReportsTo', blank=True, null=True)  # Field name made lowercase.
    photopath = models.TextField(db_column='PhotoPath', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class OrderDetails(models.Model):
    orderid = models.OneToOneField('Orders', models.DO_NOTHING, db_column='OrderID', primary_key=True)  # Field name made lowercase. The composite primary key (OrderID, ProductID) found, that is not supported. The first column is selected.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    discount = models.FloatField(db_column='Discount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order Details'


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    requireddate = models.DateTimeField(db_column='RequiredDate', blank=True, null=True)  # Field name made lowercase.
    shippeddate = models.DateTimeField(db_column='ShippedDate', blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippers', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    freight = models.TextField(db_column='Freight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shipname = models.TextField(db_column='ShipName', blank=True, null=True)  # Field name made lowercase.
    shipaddress = models.TextField(db_column='ShipAddress', blank=True, null=True)  # Field name made lowercase.
    shipcity = models.TextField(db_column='ShipCity', blank=True, null=True)  # Field name made lowercase.
    shipregion = models.TextField(db_column='ShipRegion', blank=True, null=True)  # Field name made lowercase.
    shippostalcode = models.TextField(db_column='ShipPostalCode', blank=True, null=True)  # Field name made lowercase.
    shipcountry = models.TextField(db_column='ShipCountry', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Products(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    productname = models.TextField(db_column='ProductName')  # Field name made lowercase.
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    quantityperunit = models.TextField(db_column='QuantityPerUnit', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsinstock = models.IntegerField(db_column='UnitsInStock', blank=True, null=True)  # Field name made lowercase.
    unitsonorder = models.IntegerField(db_column='UnitsOnOrder', blank=True, null=True)  # Field name made lowercase.
    reorderlevel = models.IntegerField(db_column='ReorderLevel', blank=True, null=True)  # Field name made lowercase.
    discontinued = models.TextField(db_column='Discontinued')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products'


class Regions(models.Model):
    regionid = models.AutoField(db_column='RegionID', primary_key=True)  # Field name made lowercase.
    regiondescription = models.TextField(db_column='RegionDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Regions'


class Shippers(models.Model):
    shipperid = models.AutoField(db_column='ShipperID', primary_key=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shippers'


class Suppliers(models.Model):
    supplierid = models.AutoField(db_column='SupplierID', primary_key=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName')  # Field name made lowercase.
    contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
    contacttitle = models.TextField(db_column='ContactTitle', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
    homepage = models.TextField(db_column='HomePage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Suppliers'


class Territories(models.Model):
    territoryid = models.TextField(db_column='TerritoryID', primary_key=True)  # Field name made lowercase.
    territorydescription = models.TextField(db_column='TerritoryDescription')  # Field name made lowercase.
    regionid = models.ForeignKey(Regions, models.DO_NOTHING, db_column='RegionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Territories'
