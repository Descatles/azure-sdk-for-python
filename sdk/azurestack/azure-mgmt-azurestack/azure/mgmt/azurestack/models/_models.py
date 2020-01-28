# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ActivationKeyResult(Model):
    """The resource containing the Azure Stack activation key.

    :param activation_key: Azure Stack activation key.
    :type activation_key: str
    """

    _attribute_map = {
        'activation_key': {'key': 'activationKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ActivationKeyResult, self).__init__(**kwargs)
        self.activation_key = kwargs.get('activation_key', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Compatibility(Model):
    """Product compatibility.

    :param is_compatible: Tells if product is compatible with current device
    :type is_compatible: bool
    :param message: Short error message if any compatibility issues are found
    :type message: str
    :param description: Full error message if any compatibility issues are
     found
    :type description: str
    :param issues: List of all issues found
    :type issues: list[str or
     ~azure.mgmt.azurestack.models.CompatibilityIssue]
    """

    _attribute_map = {
        'is_compatible': {'key': 'isCompatible', 'type': 'bool'},
        'message': {'key': 'message', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'issues': {'key': 'issues', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(Compatibility, self).__init__(**kwargs)
        self.is_compatible = kwargs.get('is_compatible', None)
        self.message = kwargs.get('message', None)
        self.description = kwargs.get('description', None)
        self.issues = kwargs.get('issues', None)


class Resource(Model):
    """Base resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: ID of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of Resource.
    :vartype type: str
    :param etag: The entity tag used for optimistic concurrency when modifying
     the resource.
    :type etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.etag = kwargs.get('etag', None)


class CustomerSubscription(Resource):
    """Customer subscription.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: ID of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of Resource.
    :vartype type: str
    :param etag: The entity tag used for optimistic concurrency when modifying
     the resource.
    :type etag: str
    :param tenant_id: Tenant Id.
    :type tenant_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CustomerSubscription, self).__init__(**kwargs)
        self.tenant_id = kwargs.get('tenant_id', None)


class DataDiskImage(Model):
    """Data disk image.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar lun: The LUN.
    :vartype lun: int
    :ivar source_blob_sas_uri: SAS key for source blob.
    :vartype source_blob_sas_uri: str
    """

    _validation = {
        'lun': {'readonly': True},
        'source_blob_sas_uri': {'readonly': True},
    }

    _attribute_map = {
        'lun': {'key': 'lun', 'type': 'int'},
        'source_blob_sas_uri': {'key': 'sourceBlobSasUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataDiskImage, self).__init__(**kwargs)
        self.lun = None
        self.source_blob_sas_uri = None


class DeviceConfiguration(Model):
    """Device Configuration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar device_version: Version of the device.
    :vartype device_version: str
    :ivar identity_system: Identity system of the device. Possible values
     include: 'AzureAD', 'ADFS'
    :vartype identity_system: str or ~azure.mgmt.azurestack.models.Category
    """

    _validation = {
        'device_version': {'readonly': True},
        'identity_system': {'readonly': True},
    }

    _attribute_map = {
        'device_version': {'key': 'deviceVersion', 'type': 'str'},
        'identity_system': {'key': 'identitySystem', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DeviceConfiguration, self).__init__(**kwargs)
        self.device_version = None
        self.identity_system = None


class Display(Model):
    """Contains the localized display information for this particular operation or
    action.

    :param provider: The localized, friendly version of the resource provider
     name.
    :type provider: str
    :param resource: The localized, friendly version of the resource type
     related to this action or operation; the resource type should match the
     public documentation for the resource provider.
    :type resource: str
    :param operation: The localized, friendly name for the operation. Use the
     name as it will displayed to the user.
    :type operation: str
    :param description: The localized, friendly description for the operation.
     The description will be displayed to the user. It should be thorough and
     concise for used in both tooltips and detailed views.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ErrorDetails(Model):
    """The details of the error.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None


class ErrorResponse(Model):
    """Error response indicates that the service is not able to process the
    incoming request. The reason is provided in the error message.

    :param error: The details of the error.
    :type error: ~azure.mgmt.azurestack.models.ErrorDetails
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetails'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ExtendedProduct(Model):
    """Extended description about the product required for installing it into
    Azure Stack.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar gallery_package_blob_sas_uri: The URI to the .azpkg file that
     provides information required for showing product in the gallery.
    :vartype gallery_package_blob_sas_uri: str
    :ivar product_kind: Specifies the kind of the product (virtualMachine or
     virtualMachineExtension).
    :vartype product_kind: str
    :ivar compute_role: Specifies kind of compute role included in the
     package. Possible values include: 'None', 'IaaS', 'PaaS'
    :vartype compute_role: str or ~azure.mgmt.azurestack.models.ComputeRole
    :ivar is_system_extension: Specifies if product is a Virtual Machine
     Extension.
    :vartype is_system_extension: bool
    :ivar uri: The URI.
    :vartype uri: str
    :ivar support_multiple_extensions: Indicates if specified product supports
     multiple extensions.
    :vartype support_multiple_extensions: bool
    :ivar version: Specifies product version.
    :vartype version: str
    :ivar vm_os_type: Specifies operating system used by the product. Possible
     values include: 'None', 'Windows', 'Linux'
    :vartype vm_os_type: str or ~azure.mgmt.azurestack.models.OperatingSystem
    :ivar vm_scale_set_enabled: Indicates if virtual machine Scale Set is
     enabled in the specified product.
    :vartype vm_scale_set_enabled: bool
    :ivar os_disk_image: OS disk image used by product.
    :vartype os_disk_image: ~azure.mgmt.azurestack.models.OsDiskImage
    :ivar data_disk_images: List of attached data disks.
    :vartype data_disk_images:
     list[~azure.mgmt.azurestack.models.DataDiskImage]
    """

    _validation = {
        'gallery_package_blob_sas_uri': {'readonly': True},
        'product_kind': {'readonly': True},
        'compute_role': {'readonly': True},
        'is_system_extension': {'readonly': True},
        'uri': {'readonly': True},
        'support_multiple_extensions': {'readonly': True},
        'version': {'readonly': True},
        'vm_os_type': {'readonly': True},
        'vm_scale_set_enabled': {'readonly': True},
        'os_disk_image': {'readonly': True},
        'data_disk_images': {'readonly': True},
    }

    _attribute_map = {
        'gallery_package_blob_sas_uri': {'key': 'galleryPackageBlobSasUri', 'type': 'str'},
        'product_kind': {'key': 'productKind', 'type': 'str'},
        'compute_role': {'key': 'properties.computeRole', 'type': 'str'},
        'is_system_extension': {'key': 'properties.isSystemExtension', 'type': 'bool'},
        'uri': {'key': 'properties.sourceBlob.uri', 'type': 'str'},
        'support_multiple_extensions': {'key': 'properties.supportMultipleExtensions', 'type': 'bool'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'vm_os_type': {'key': 'properties.vmOsType', 'type': 'str'},
        'vm_scale_set_enabled': {'key': 'properties.vmScaleSetEnabled', 'type': 'bool'},
        'os_disk_image': {'key': 'properties.osDiskImage', 'type': 'OsDiskImage'},
        'data_disk_images': {'key': 'properties.dataDiskImages', 'type': '[DataDiskImage]'},
    }

    def __init__(self, **kwargs):
        super(ExtendedProduct, self).__init__(**kwargs)
        self.gallery_package_blob_sas_uri = None
        self.product_kind = None
        self.compute_role = None
        self.is_system_extension = None
        self.uri = None
        self.support_multiple_extensions = None
        self.version = None
        self.vm_os_type = None
        self.vm_scale_set_enabled = None
        self.os_disk_image = None
        self.data_disk_images = None


class IconUris(Model):
    """Links to product icons.

    :param large: URI to large icon.
    :type large: str
    :param wide: URI to wide icon.
    :type wide: str
    :param medium: URI to medium icon.
    :type medium: str
    :param small: URI to small icon.
    :type small: str
    :param hero: URI to hero icon.
    :type hero: str
    """

    _attribute_map = {
        'large': {'key': 'large', 'type': 'str'},
        'wide': {'key': 'wide', 'type': 'str'},
        'medium': {'key': 'medium', 'type': 'str'},
        'small': {'key': 'small', 'type': 'str'},
        'hero': {'key': 'hero', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IconUris, self).__init__(**kwargs)
        self.large = kwargs.get('large', None)
        self.wide = kwargs.get('wide', None)
        self.medium = kwargs.get('medium', None)
        self.small = kwargs.get('small', None)
        self.hero = kwargs.get('hero', None)


class MarketplaceProductLogUpdate(Model):
    """Update details for product log.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar operation: Operation to log.
    :vartype operation: str
    :ivar status: Operation status to log.
    :vartype status: str
    :ivar error: Error related to the operation.
    :vartype error: str
    :ivar details: Error details related to operation.
    :vartype details: str
    """

    _validation = {
        'operation': {'readonly': True},
        'status': {'readonly': True},
        'error': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'operation': {'key': 'operation', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'error': {'key': 'error', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MarketplaceProductLogUpdate, self).__init__(**kwargs)
        self.operation = None
        self.status = None
        self.error = None
        self.details = None


class Operation(Model):
    """Describes the supported REST operation.

    :param name: The name of the operation being performed on this particular
     object.
    :type name: str
    :param display: Contains the localized display information for this
     particular operation or action.
    :type display: ~azure.mgmt.azurestack.models.Display
    :param origin: The intended executor of the operation.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'Display'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)


class OsDiskImage(Model):
    """OS disk image.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar operating_system: OS operating system type. Possible values include:
     'None', 'Windows', 'Linux'
    :vartype operating_system: str or
     ~azure.mgmt.azurestack.models.OperatingSystem
    :ivar source_blob_sas_uri: SAS key for source blob.
    :vartype source_blob_sas_uri: str
    """

    _validation = {
        'operating_system': {'readonly': True},
        'source_blob_sas_uri': {'readonly': True},
    }

    _attribute_map = {
        'operating_system': {'key': 'operatingSystem', 'type': 'str'},
        'source_blob_sas_uri': {'key': 'sourceBlobSasUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OsDiskImage, self).__init__(**kwargs)
        self.operating_system = None
        self.source_blob_sas_uri = None


class Product(Resource):
    """Product information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: ID of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of Resource.
    :vartype type: str
    :param etag: The entity tag used for optimistic concurrency when modifying
     the resource.
    :type etag: str
    :param display_name: The display name of the product.
    :type display_name: str
    :param description: The description of the product.
    :type description: str
    :param publisher_display_name: The user-friendly name of the product
     publisher.
    :type publisher_display_name: str
    :param publisher_identifier: Publisher identifier.
    :type publisher_identifier: str
    :param offer: The offer representing the product.
    :type offer: str
    :param offer_version: The version of the product offer.
    :type offer_version: str
    :param sku: The product SKU.
    :type sku: str
    :param billing_part_number: The part number used for billing purposes.
    :type billing_part_number: str
    :param vm_extension_type: The type of the Virtual Machine Extension.
    :type vm_extension_type: str
    :param gallery_item_identity: The identifier of the gallery item
     corresponding to the product.
    :type gallery_item_identity: str
    :param icon_uris: Additional links available for this product.
    :type icon_uris: ~azure.mgmt.azurestack.models.IconUris
    :param links: Additional links available for this product.
    :type links: list[~azure.mgmt.azurestack.models.ProductLink]
    :param legal_terms: The legal terms.
    :type legal_terms: str
    :param privacy_policy: The privacy policy.
    :type privacy_policy: str
    :param payload_length: The length of product content.
    :type payload_length: long
    :param product_kind: The kind of the product (virtualMachine or
     virtualMachineExtension)
    :type product_kind: str
    :param product_properties: Additional properties for the product.
    :type product_properties: ~azure.mgmt.azurestack.models.ProductProperties
    :param compatibility: Product compatibility with current device.
    :type compatibility: ~azure.mgmt.azurestack.models.Compatibility
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'publisher_display_name': {'key': 'properties.publisherDisplayName', 'type': 'str'},
        'publisher_identifier': {'key': 'properties.publisherIdentifier', 'type': 'str'},
        'offer': {'key': 'properties.offer', 'type': 'str'},
        'offer_version': {'key': 'properties.offerVersion', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'str'},
        'billing_part_number': {'key': 'properties.billingPartNumber', 'type': 'str'},
        'vm_extension_type': {'key': 'properties.vmExtensionType', 'type': 'str'},
        'gallery_item_identity': {'key': 'properties.galleryItemIdentity', 'type': 'str'},
        'icon_uris': {'key': 'properties.iconUris', 'type': 'IconUris'},
        'links': {'key': 'properties.links', 'type': '[ProductLink]'},
        'legal_terms': {'key': 'properties.legalTerms', 'type': 'str'},
        'privacy_policy': {'key': 'properties.privacyPolicy', 'type': 'str'},
        'payload_length': {'key': 'properties.payloadLength', 'type': 'long'},
        'product_kind': {'key': 'properties.productKind', 'type': 'str'},
        'product_properties': {'key': 'properties.productProperties', 'type': 'ProductProperties'},
        'compatibility': {'key': 'properties.compatibility', 'type': 'Compatibility'},
    }

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.publisher_display_name = kwargs.get('publisher_display_name', None)
        self.publisher_identifier = kwargs.get('publisher_identifier', None)
        self.offer = kwargs.get('offer', None)
        self.offer_version = kwargs.get('offer_version', None)
        self.sku = kwargs.get('sku', None)
        self.billing_part_number = kwargs.get('billing_part_number', None)
        self.vm_extension_type = kwargs.get('vm_extension_type', None)
        self.gallery_item_identity = kwargs.get('gallery_item_identity', None)
        self.icon_uris = kwargs.get('icon_uris', None)
        self.links = kwargs.get('links', None)
        self.legal_terms = kwargs.get('legal_terms', None)
        self.privacy_policy = kwargs.get('privacy_policy', None)
        self.payload_length = kwargs.get('payload_length', None)
        self.product_kind = kwargs.get('product_kind', None)
        self.product_properties = kwargs.get('product_properties', None)
        self.compatibility = kwargs.get('compatibility', None)


class ProductLink(Model):
    """Link with additional information about a product.

    :param display_name: The description of the link.
    :type display_name: str
    :param uri: The URI corresponding to the link.
    :type uri: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProductLink, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.uri = kwargs.get('uri', None)


class ProductList(Model):
    """Pageable list of products.

    :param next_link: URI to the next page.
    :type next_link: str
    :param value: List of products.
    :type value: list[~azure.mgmt.azurestack.models.Product]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Product]'},
    }

    def __init__(self, **kwargs):
        super(ProductList, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs.get('value', None)


class ProductLog(Model):
    """Product action log.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Log ID.
    :vartype id: str
    :ivar product_id: Logged product ID.
    :vartype product_id: str
    :ivar subscription_id: Logged subscription ID.
    :vartype subscription_id: str
    :ivar registration_name: Logged registration name.
    :vartype registration_name: str
    :ivar resource_group_name: Logged resource group name.
    :vartype resource_group_name: str
    :ivar operation: Logged operation.
    :vartype operation: str
    :ivar start_date: Operation start datetime.
    :vartype start_date: str
    :ivar end_date: Operation end datetime.
    :vartype end_date: str
    :ivar status: Operation status.
    :vartype status: str
    :ivar error: Operation error data.
    :vartype error: str
    :ivar details: Operation error details.
    :vartype details: str
    """

    _validation = {
        'id': {'readonly': True},
        'product_id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'registration_name': {'readonly': True},
        'resource_group_name': {'readonly': True},
        'operation': {'readonly': True},
        'start_date': {'readonly': True},
        'end_date': {'readonly': True},
        'status': {'readonly': True},
        'error': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'product_id': {'key': 'productId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'registration_name': {'key': 'registrationName', 'type': 'str'},
        'resource_group_name': {'key': 'resourceGroupName', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'error': {'key': 'error', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProductLog, self).__init__(**kwargs)
        self.id = None
        self.product_id = None
        self.subscription_id = None
        self.registration_name = None
        self.resource_group_name = None
        self.operation = None
        self.start_date = None
        self.end_date = None
        self.status = None
        self.error = None
        self.details = None


class ProductProperties(Model):
    """Additional properties of the product.

    :param version: The version.
    :type version: str
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProductProperties, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)


class TrackedResource(Model):
    """Base resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: ID of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of Resource.
    :vartype type: str
    :ivar location: Required. Location of the resource. Default value:
     "global" .
    :vartype location: str
    :param tags: Custom tags for the resource.
    :type tags: dict[str, str]
    :param etag: The entity tag used for optimistic concurrency when modifying
     the resource.
    :type etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    location = "global"

    def __init__(self, **kwargs):
        super(TrackedResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.etag = kwargs.get('etag', None)


class Registration(TrackedResource):
    """Registration information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: ID of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of Resource.
    :vartype type: str
    :ivar location: Required. Location of the resource. Default value:
     "global" .
    :vartype location: str
    :param tags: Custom tags for the resource.
    :type tags: dict[str, str]
    :param etag: The entity tag used for optimistic concurrency when modifying
     the resource.
    :type etag: str
    :param object_id: The object identifier associated with the Azure Stack
     connecting to Azure.
    :type object_id: str
    :param cloud_id: The identifier of the registered Azure Stack.
    :type cloud_id: str
    :param billing_model: Specifies the billing mode for the Azure Stack
     registration.
    :type billing_model: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'object_id': {'key': 'properties.objectId', 'type': 'str'},
        'cloud_id': {'key': 'properties.cloudId', 'type': 'str'},
        'billing_model': {'key': 'properties.billingModel', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Registration, self).__init__(**kwargs)
        self.object_id = kwargs.get('object_id', None)
        self.cloud_id = kwargs.get('cloud_id', None)
        self.billing_model = kwargs.get('billing_model', None)


class RegistrationParameter(Model):
    """Registration resource.

    All required parameters must be populated in order to send to Azure.

    :param registration_token: Required. The token identifying registered
     Azure Stack
    :type registration_token: str
    :param location: Location of the resource. Possible values include:
     'global'
    :type location: str or ~azure.mgmt.azurestack.models.Location
    """

    _validation = {
        'registration_token': {'required': True},
    }

    _attribute_map = {
        'registration_token': {'key': 'properties.registrationToken', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RegistrationParameter, self).__init__(**kwargs)
        self.registration_token = kwargs.get('registration_token', None)
        self.location = kwargs.get('location', None)


class VirtualMachineExtensionProductProperties(Model):
    """Product information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar compute_role: Specifies kind of compute role included in the
     package. Possible values include: 'None', 'IaaS', 'PaaS'
    :vartype compute_role: str or ~azure.mgmt.azurestack.models.ComputeRole
    :ivar is_system_extension: Specifies if product is a Virtual Machine
     Extension.
    :vartype is_system_extension: bool
    :ivar uri: The URI.
    :vartype uri: str
    :ivar support_multiple_extensions: Indicates if specified product supports
     multiple extensions.
    :vartype support_multiple_extensions: bool
    :ivar version: Specifies product version.
    :vartype version: str
    :ivar vm_os_type: Specifies operating system used by the product. Possible
     values include: 'None', 'Windows', 'Linux'
    :vartype vm_os_type: str or ~azure.mgmt.azurestack.models.OperatingSystem
    :ivar vm_scale_set_enabled: Indicates if virtual machine Scale Set is
     enabled in the specified product.
    :vartype vm_scale_set_enabled: bool
    """

    _validation = {
        'compute_role': {'readonly': True},
        'is_system_extension': {'readonly': True},
        'uri': {'readonly': True},
        'support_multiple_extensions': {'readonly': True},
        'version': {'readonly': True},
        'vm_os_type': {'readonly': True},
        'vm_scale_set_enabled': {'readonly': True},
    }

    _attribute_map = {
        'compute_role': {'key': 'computeRole', 'type': 'str'},
        'is_system_extension': {'key': 'isSystemExtension', 'type': 'bool'},
        'uri': {'key': 'sourceBlob.uri', 'type': 'str'},
        'support_multiple_extensions': {'key': 'supportMultipleExtensions', 'type': 'bool'},
        'version': {'key': 'version', 'type': 'str'},
        'vm_os_type': {'key': 'vmOsType', 'type': 'str'},
        'vm_scale_set_enabled': {'key': 'vmScaleSetEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineExtensionProductProperties, self).__init__(**kwargs)
        self.compute_role = None
        self.is_system_extension = None
        self.uri = None
        self.support_multiple_extensions = None
        self.version = None
        self.vm_os_type = None
        self.vm_scale_set_enabled = None


class VirtualMachineProductProperties(Model):
    """Product information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar version: Specifies product version.
    :vartype version: str
    :ivar os_disk_image: OS disk image used by product.
    :vartype os_disk_image: ~azure.mgmt.azurestack.models.OsDiskImage
    :ivar data_disk_images: List of attached data disks.
    :vartype data_disk_images:
     list[~azure.mgmt.azurestack.models.DataDiskImage]
    """

    _validation = {
        'version': {'readonly': True},
        'os_disk_image': {'readonly': True},
        'data_disk_images': {'readonly': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'os_disk_image': {'key': 'osDiskImage', 'type': 'OsDiskImage'},
        'data_disk_images': {'key': 'dataDiskImages', 'type': '[DataDiskImage]'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineProductProperties, self).__init__(**kwargs)
        self.version = None
        self.os_disk_image = None
        self.data_disk_images = None