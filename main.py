import cluster.service.attribute.get as get_attributes_
import cluster.service.attribute.create as create_attribute_
import cluster.service.attribute.update as update_attribute_
import cluster.service.attribute.delete as delete_attribute_

import cluster.service.attribute_set.get as get_attribute_set_
import cluster.service.attribute_set.create as create_attribute_set_
import cluster.service.attribute_set.update as update_attribute_set_
import cluster.service.attribute_set.delete as delete_attribute_set_
import cluster.service.attribute_set.link as link_attribute_set_
import cluster.service.attribute_set.unlink as unlink_attribute_set_

import cluster.service.entity.get as get_entity_
import cluster.service.entity.create as create_entity_
import cluster.service.entity.update as update_entity_
import cluster.service.entity.delete as delete_entity_

from fastapi import FastAPI
from pydantic import BaseModel


class AttributeData(BaseModel):
    name: str
    attribute_type: str
    source_model: str = None


class EntityData(BaseModel):
    attribute_set_id: str
    entity_type: str = "default"
    attributes: dict = {}


class UpdateEntityData(BaseModel):
    entity_id: str
    attribute_set_id: str
    entity_type: str = "default"
    attributes: dict = {}


class AttributeSetData(BaseModel):
    name: str


class UpdateAttributeData(BaseModel):
    attribute_id: str
    name: str
    attribute_type: str
    source_model: str = None


class UpdateAttributeSetData(BaseModel):
    attribute_set_id: str
    name: str


class DeleteAttributeData(BaseModel):
    attribute_id: str


class DeleteAttributeSetData(BaseModel):
    attribute_set_id: str


class DeleteEntityData(BaseModel):
    entity_id: str


class LinkAttributeSetData(BaseModel):
    attribute_set_id: str
    attribute_id: str


class UnlinkAttributeSetData(BaseModel):
    attribute_set_id: str
    attribute_id: str


class Filters(BaseModel):
    filters: list = None


app = FastAPI()


@app.post("/service/attribute/load", tags=["attribute"])
async def get_attribute(filters: Filters):
    return get_attributes_.execute(filters.filters)


@app.post("/service/attribute/create", tags=["attribute"])
async def create_attribute(attribute_data: AttributeData):
    return create_attribute_.execute(
        {
            "name": attribute_data.name,
            "attribute_type": attribute_data.attribute_type,
            "source_model": attribute_data.source_model,
        }
    )


@app.put("/service/attribute/update", tags=["attribute"])
async def update_attribute(attribute_data: UpdateAttributeData):
    return update_attribute_.execute(
        {
            "attribute_id": attribute_data.attribute_id,
            "name": attribute_data.name,
            "attribute_type": attribute_data.attribute_type,
            "source_model": attribute_data.source_model,
        }
    )


@app.delete("/service/attribute/delete", tags=["attribute"])
async def delete_attribute(delete_attribute_data: DeleteAttributeData):
    return delete_attribute_.execute(
        {
            "attribute_id": delete_attribute_data.attribute_id
        }
    )


@app.post("/service/attribute-set/load", tags=["attribute-set"])
async def get_attribute_set(filters: Filters):
    return get_attribute_set_.execute(filters.filters)


@app.post("/service/attribute-set/create", tags=["attribute-set"])
async def create_attribute_set(attribute_set_data: AttributeSetData):
    return create_attribute_set_.execute(
        {
            "name": attribute_set_data.name,
        }
    )


@app.put("/service/attribute-set/update", tags=["attribute-set"])
async def update_attribute_set(attribute_set_data: UpdateAttributeSetData):
    return update_attribute_set_.execute(
        {
            "attribute_set_id": attribute_set_data.attribute_set_id,
            "name": attribute_set_data.name,
        }
    )


@app.delete("/service/attribute-set/delete", tags=["attribute-set"])
async def delete_attribute_set(delete_attribute_set_data: DeleteAttributeSetData):
    return delete_attribute_set_.execute(
        {
            "attribute_set_id": delete_attribute_set_data.attribute_set_id
        }
    )


@app.post("/service/attribute-set/link", tags=["attribute-set"])
async def link_attribute_set(link_attribute_set_data: LinkAttributeSetData):
    return link_attribute_set_.execute(
        {
            "attribute_set_id": link_attribute_set_data.attribute_set_id,
            "attribute_id": link_attribute_set_data.attribute_id,
        }
    )


@app.post("/service/attribute-set/unlink", tags=["attribute-set"])
async def unlink_attribute_set(unlink_attribute_set_data: UnlinkAttributeSetData):
    return unlink_attribute_set_.execute(
        {
            "attribute_set_id": unlink_attribute_set_data.attribute_set_id,
            "attribute_id": unlink_attribute_set_data.attribute_id,
        }
    )


@app.post("/service/entity/load", tags=["entity"])
async def get_entity(filters: Filters):
    return get_entity_.execute(filters.filters)


@app.post("/service/entity/create", tags=["entity"])
async def create_entity(entity_data: EntityData):
    return create_entity_.execute(
        {
            "entity_type": entity_data.entity_type,
            "attribute_set_id": entity_data.attribute_set_id,
            "attributes": entity_data.attributes,
        }
    )


@app.put("/service/entity/update", tags=["entity"])
async def update_entity(update_entity_data: UpdateEntityData):
    return update_entity_.execute(
        {
            "entity_id": update_entity_data.entity_id,
            "entity_type": update_entity_data.entity_type,
            "attribute_set_id": update_entity_data.attribute_set_id,
            "attributes": update_entity_data.attributes,
        }
    )


@app.delete("/service/entity/delete", tags=["entity"])
async def delete_entity(delete_entity_data: DeleteEntityData):
    return delete_entity_.execute(
        {
            "entity_id": delete_entity_data.entity_id,
        }
    )
