from django.core.paginator import Paginator
from core.models import BaseModel


class BaseDAO():
    """Base class for Data Access Objects.
    Provides helper functions for accessing data from the database.

    Concrete classes must override the following class variables:
    MODEL_CLASS: The Django Model object that this DAO is abstracting
    BATCH_SIZE: The number of models to handle in batch operations
    """

    ### Override these in concrete implementations ###
    MODEL_CLASS = BaseModel
    BATCH_SIZE = 1000
    
    @classmethod
    def create(cls, construct_params, save=True):
        """Create an instance of the model.
        :param construct_params: Key-value arguments for the model constructor
        :type construct_params: dict
        :param save: Whether to immediately persist the object in the DB
        :type save: bool
        :return: An instance of the model
        :rtype: BaseModel
        """
        instance = cls.MODEL_CLASS(**construct_params)
        if save:
            cls.save(instance)
        return instance

    @classmethod
    def save(cls, model):
        """Creates or updates a model instance in the DB.
        :param model: An instance of the model
        :type model: BaseModel
        :return: True if the model was saved
        :rtype: bool
        """
        if model and type(model) is cls.MODEL_CLASS:
            model.save()
            return True
        return False
 
    @classmethod
    def save_batch(cls, models, batch_size=BATCH_SIZE):
        """Creates or updates a batch of model instances in the DB.
        :param models: An list of models
        :type models: list[BaseModel]
        :return: True if the models were saved
        :rtype: bool
        """
        if models and all(isinstance(model, cls.MODEL_CLASS) for model in models):
            cls.MODEL_CLASS.objects.bulk_create(models, batch_size=batch_size)
            return True
        return False
 
    @classmethod
    def delete(cls, model):
        """Deletes the model instance from the DB.
        :param model: An instance of the model
        :type model: BaseModel
        :return: True if the model was deleted
        :rtype: bool
        """
        if model and type(model) is cls.MODEL_CLASS:
            model.delete()
            return True
        return False
    
    @classmethod
    def delete_batch(cls, models):
        """Deletes a batch of model instances from the DB.
        :param models: An list of models
        :type models: list[BaseModel]
        :return: True if the models were deleted
        :rtype: bool
        """
        if models and all(isinstance(model, cls.MODEL_CLASS) for model in models):
            for model in models:
                model.delete()
            return True
        return False
 
    @classmethod
    def delete_batch_by_query(cls, filters: dict, exclude: dict):
        """Deletes a batch of model instances from the DB using a query.
        :param filters: Key-value arguments to filter the models
        :type filters: dict
        :param exclude: Key-value arguments for the exclude filters
        :type exclude: dict
        :return: True if the models were deleted
        :rtype: bool
        """
        cls.MODEL_CLASS.objects.filter(**filters).exclude(**exclude).delete()
        return True

    @classmethod
    def find_queryset(cls, filters: dict, exclude={}, order={}):
        """
        :param filters: Key-value arguments to filter the models
        :type filters: dict
        :param exclude: Key-value arguments for the exclude filters
        :type exclude: dict
        :param order: What to order results by
        :type order: list|str
        :return: A list of models found
        :rtype: list[BaseModel]
        """
        queryset = cls.MODEL_CLASS.objects.filter(**filters).exclude(**exclude)
        if order:
            if type(order) is list:
                queryset = queryset.order_by(*order)
            else:
                queryset = queryset.order_by(order)
        return queryset
 
    @classmethod
    def find_one(cls, filters: dict, exclude: dict, order):
        """
        :param filters: Key-value arguments to filter the models
        :type filters: dict
        :param exclude: Key-value arguments for the exclude filters
        :type exclude: dict
        :param order: What to order results by
        :type order: list|str
        :return: The first model found, or None
        :rtype: BaseModel
        """
        return cls.find_queryset(filters, exclude, order).first()
    
    @classmethod
    def find_all(cls, filters: dict, exclude: dict, order):
        """
        :param filters: Key-value arguments to filter the models
        :type filters: dict
        :param exclude: Key-value arguments for the exclude filters
        :type exclude: dict
        :param order: What to order results by
        :type order: list|str
        :return: A list of models found
        :rtype: list[BaseModel]
        """
        return cls.find_queryset(filters, exclude, order).all()

    @classmethod
    def find_some(cls, filters: dict, exclude: dict, order, limit, offset):
        """
        :param filters: Key-value arguments to filter the models
        :type filters: dict
        :param exclude: Key-value arguments for the exclude filters
        :type exclude: dict
        :param order: What to order results by
        :type order: list|str
        :param limit: How many results to return per page
        :type limit: int
        :param offset: Which page of results to return
        :type offset: int
        :return: A list of models found
        :rtype: list[BaseModel]
        """
        queryset = cls.find_queryset(filters, exclude, order)
        return Paginator(queryset, limit).page(offset)

    @classmethod
    def exists_query(cls, filters: dict, exclude: dict, order):
        """
        :param filters: Key-value arguments to filter the models
        :type filters: dict
        :param exclude: Key-value arguments for the exclude filters
        :type exclude: dict
        :param order: What to order results by
        :type order: list|str
        :return: Whether a model exists with these filters in the DB
        :rtype: bool
        """
        return cls.MODEL_CLASS.objects.filter(**filters).exclude(**exclude).exists()
    
    @classmethod
    def exists_instance(cls, model):
        """
        :param model: A model instance
        :type model: BaseModel
        :return: Whether a model exists in the DB
        :rtype: bool
        """
        if model.id:
            return True
        return False
    
    @classmethod
    def count(cls, filters: dict, exclude: dict):
        """
        :param filters: Key-value arguments to filter the models
        :type filters: dict
        :param exclude: Key-value arguments for the exclude filters
        :type exclude: dict
        :return: How many models exist with these filters in the DB
        :rtype: int
        """
        return cls.MODEL_CLASS.objects.filter(**filters).exclude(**exclude).count()
 