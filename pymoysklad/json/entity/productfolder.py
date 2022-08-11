from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.enums import GenderEnum
from pymoysklad.json.meta import Meta
from pymoysklad.json.utils.types import CollectionAnswer, MetaInMeta


@dataclass(repr=False)
class ProductFolder(object.Entity):
    archived: bool | None = None
    code: str | None = None
    description: str | None = None
    effectiveVat: int | None = None
    effectiveVatEnabled: bool | None = None
    group: MetaInMeta | None = None
    name: str | None = None
    owner: MetaInMeta | None = None
    pathName: str | None = None
    taxSystem: str | None = None  # TODO: Create ENUM
    useParentVat: bool | None = None
    vat: int | None = None
    vatEnabled: bool | None = None
    productFolder: ProductFolder | MetaInMeta | None = None

class ProductFolderMethods(object.ObjectMethods):
    NAME = "productfolder"

    def list_product_folder(self, **kwargs) -> CollectionAnswer[ProductFolder]:
        return self.client.get_collection(self.NAME, ProductFolder, **kwargs)

    def get_product_folder(self, uuid: UUID) -> ProductFolder:
        return self.client.get_entity(self.NAME, ProductFolder, uuid)

    def create_product_folder(self, product_folders: ProductFolder | list[ProductFolder]):
        if isinstance(product_folders, list):
            return self.client.mass_create_entity(self.NAME, product_folders)
        else:
            return self.client.create_entity(self.NAME, product_folders)

    def delete_product_folder(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_product_folder(self, uuid, product_folder: ProductFolder) -> ProductFolder:
        return self.client.edit_entity(self.NAME, product_folder, uuid)

    def mass_delete_product_folder(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)
