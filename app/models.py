from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Network(models.Model):
    name = models.CharField(max_length=50)

class Show(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    network = models.ForeignKey(Network, on_delete=models.PROTECT)
    show = models.CharField(max_length=50)

# def create_provider(name):
#     name = Provider(name=name)
#     name.save()
#     return name

# def create_network(name):
#     name = Network(name=name)
#     name.save()
#     return name

# def create_show(provider, network, show):
#     tv = Show(provider, network, show)
#     tv.save()
#     return tv

# def read_all():
#     return Show.objects.all()

# def find_network_by_name(network):
#     error_message = 'Network does not exist.'
#     try: 
#         return Network.objects.get(network=network)
#     except Network.DoesNotExist:
#         return error_message

# def find_provider_by_name(provider):
#     error = 'Provider does not exist.'
#     try: 
#         return Provider.objects.get(provider=provider)
#     except Provider.DoesNotExist:
#         return error

# def find_show_by_name(show):
#     message = 'Show does not exist.'
#     try: 
#         return Show.objects.get(show=show)
#     except Show.DoesNotExist:
#         return message

# def update_show(show, new_show):
#     message = 'Show does not exist.'
#     not_error = 'Show updated!'
#     try:
#         tv = find_show_by_name(show)
#         tv.show = new_show
#         tv.save()
#         return not_error
#     except Show.DoesNotExist:
#         return message

# def update_network(network, new_net):
#     not_error = "Network updated!"
#     message = 'Network does not exist.'
#     try:
#         net = find_network_by_name(network)
#         net.name = new_net
#         net.save()
#         return not_error
#     except Network.DoesNotExist:
#         return message

# def delete_show(show):
#     not_error = "Show deleted!"
#     message = 'Show does not exist.'
#     try:
#         tv = find_show_by_name(show)
#         tv.delete()
#         return not_error
#     except Show.DoesNotExist:
#         return message

# def delete_network(network):
#     message = "Network deleted!"
#     error_message = 'Network does not exist.'
#     try: 
#         net = find_network_by_name(network)
#         net.delete()
#         return message
#     except Network.DoesNotExist:
#         return error_message