# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import Optional
from datetime import datetime
from enum import Enum

from sqlmodel import Field, Relationship

from pydevlake.model import DomainModel, DomainScope, NoPKModel


class CicdScope(DomainScope, table=True):
    __tablename__ = 'cicd_scopes'

    name: str
    description: Optional[str]
    url: Optional[str]
    createdDate: Optional[datetime]
    updatedDate: Optional[datetime]


class CICDPipeline(DomainModel, table=True):
    __table_name__ = 'cicd_pipelines'

    class Result(Enum):
        SUCCESS = "SUCCESS"
        FAILURE = "FAILURE"
        ABORT = "ABORT"
        MANUAL = "MANUAL"

    class Status(Enum):
        IN_PROGRESS = "IN_PROGRESS"
        DONE = "DONE"
        MANUAL = "MANUAL"

    class Type(Enum):
        CI = "CI"
        CD = "CD"

    name: str
    status: Status
    created_date: datetime
    finished_date: Optional[datetime]
    result: Optional[Result]
    duration_sec: Optional[int]
    environment: Optional[str]
    type: Optional[Type] #Unused

    # parent_pipelines: list["CICDPipeline"] = Relationship(back_populates="child_pipelines", link_model="CICDPipelineRelationship")
    # child_pipelines: list["CICDPipeline"] = Relationship(back_populates="parent_pipelines", link_model="CICDPipelineRelationship")


class CICDPipelineRelationship(NoPKModel):
    __table_name__ = 'cicd_pipeline_relationships'
    parent_pipeline_id: str = Field(primary_key=True, foreign_key=CICDPipeline.id)
    child_pipeline_id: str = Field(primary_key=True, foreign_key=CICDPipeline.id)
