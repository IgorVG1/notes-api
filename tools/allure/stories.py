from enum import Enum


class AllureStory(str, Enum):

    LOGIN = "Login"

    GET_ENTITY = "Get entity"
    GET_ENTITIES = "Get entities"
    CREATE_ENTITY = "Create entity"
    PART_UPDATE_ENTITY = "Part update entity"
    FULL_UPDATE_ENTITY = "Full update entity"
    DELETE_ENTITY = "Delete entity"
    VALIDATE_ENTITY = "Validate entity"