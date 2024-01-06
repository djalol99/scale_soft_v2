from django.urls import path
from . import views


app_name = 'catalogs'

urlpatterns = [
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand-create'),
    path('brands/update/<int:pk>/', views.BrandUpdateView.as_view(), name='brand-update'),
    path('brands/delete/<int:pk>/', views.BrandDeleteView.as_view(), name='brand-delete'),
    path('vehicles/', views.VehicleListView.as_view(), name='vehicles'),
    path('vehicles/create/', views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicles/update/<int:pk>/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='vehicle-delete'),
    path('organizations/', views.OrganizationListView.as_view(), name='organizations'),
    path('organizations/create/', views.OrganizationCreateView.as_view(), name='organization-create'),
    path('organizations/update/<int:pk>/', views.OrganizationUpdateView.as_view(), name='organization-update'),
    path('organizations/delete/<int:pk>/', views.OrganizationDeleteView.as_view(), name='organization-delete'),
    path('warehouses/', views.WarehouseListView.as_view(), name='warehouses'),
    path('warehouses/create/', views.WarehouseCreateView.as_view(), name='warehouse-create'),
    path('warehouses/update/<int:pk>/', views.WarehouseUpdateView.as_view(), name='warehouse-update'),
    path('warehouses/delete/<int:pk>/', views.WarehouseDeleteView.as_view(), name='warehouse-delete'),
    path('counterparties/', views.CounterpartyListView.as_view(), name='counterparties'),
    path('counterparties/create/', views.CounterpartyCreateView.as_view(), name='counterparty-create'),
    path('counterparties/update/<int:pk>/', views.CounterpartyUpdateView.as_view(), name='counterparty-update'),
    path('counterparties/delete/<int:pk>/', views.CounterpartyDeleteView.as_view(), name='counterparty-delete'),
    path('contracts/', views.ContractListView.as_view(), name='contracts'),
    path('contracts/create/', views.ContractCreateView.as_view(), name='contract-create'),
    path('contracts/update/<int:pk>/', views.ContractUpdateView.as_view(), name='contract-update'),
    path('contracts/delete/<int:pk>/', views.ContractDeleteView.as_view(), name='contract-delete'),
    path('drivers/', views.DriverListView.as_view(), name='drivers'),
    path('drivers/create/', views.DriverCreateView.as_view(), name='driver-create'),
    path('drivers/update/<int:pk>/', views.DriverUpdateView.as_view(), name='driver-update'),
    path('drivers/delete/<int:pk>/', views.DriverDeleteView.as_view(), name='driver-delete'),
    path('uom/', views.UOMListView.as_view(), name='uom'),
    path('uom/create/', views.UOMCreateView.as_view(), name='uom-create'),
    path('uom/update/<int:pk>/', views.UOMUpdateView.as_view(), name='uom-update'),
    path('uom/delete/<int:pk>/', views.UOMDeleteView.as_view(), name='uom-delete'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]

