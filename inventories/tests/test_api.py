import random

from django.test import TestCase
from django.urls import reverse

from inventories.models import Warehouse

from users.models import User


class TestApi(TestCase):
    """ Basic tests"""
    def setUp(self):
        self.usuario = User.objects.create_superuser("prueba3@gmail.com",
                                                     "root")
        self.warehouse_dummy = Warehouse(
            description='for testing in another way')
        self.warehouse_dummy.save()
        self.get_inventory_list_url = reverse('inventories-list')
        self.create_inventory_url = reverse('inventories-list')
        self.create_warehouse_url = reverse('warehouses-list')
        self.get_warehouse_list_url = reverse('warehouses-list')
        self.get_auth_url = reverse('auth-list')
        self.inventory_data = {
            'stock': 3000.00,
            'warehouse': self.warehouse_dummy.id
        }
        self.warehouse_data = {
            'description': 'This is for testing'
        }
        self.correct_whs_data_update = {
            'status': False
        }
        self.usuario_dummy = User.objects.get(email="prueba3@gmail.com")
        self.user_data = {
            "email": self.usuario_dummy.email,
            "password": "root"
        }

    def test_fails_to_register_without_data_no_token(self):
        res = self.client.post(self.create_inventory_url)
        self.assertEqual(res.status_code, 401)

    def test_fails_to_register_without_data_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.post(self.create_inventory_url,
                                   HTTP_AUTHORIZATION=auth)
            self.assertEqual(res.status_code, 400)

    def test_gets_correctly_inventories(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.get(
                self.get_inventory_list_url, HTTP_AUTHORIZATION=auth)
            self.assertEqual(res.status_code, 200)

    def test_cannot_register_warehouse_without_data_no_token(self):
        res = self.client.post(self.create_warehouse_url)
        self.assertEqual(res.status_code, 401)

    def test_cannot_register_warehouse_without_data_token_success(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.post(self.create_warehouse_url,
                                   HTTP_AUTHORIZATION=auth)
            self.assertEqual(res.status_code, 400)

    def test_can_register_warehouse_with_data_no_token(self):
        res = self.client.post(self.create_warehouse_url, self.warehouse_data)
        self.assertEqual(res.status_code, 401)

    def test_can_register_warehouse_with_data_token_success(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.post(self.create_warehouse_url,
                                   self.warehouse_data,
                                   HTTP_AUTHORIZATION=auth)
            self.assertEqual(res.status_code, 201)

    def test_can_retrieve_warehouses_list_no_token(self):
        res = self.client.get(self.get_warehouse_list_url)
        self.assertEqual(res.status_code, 401)

    def test_can_retrieve_warehouses_list_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.get(self.get_warehouse_list_url,
                                  HTTP_AUTHORIZATION=auth)
            self.assertEqual(res.status_code, 200)

    def test_register_correctly_with_data_no_token(self):
        res = self.client.post(self.create_inventory_url, self.inventory_data)
        self.assertEqual(res.status_code, 401)

    def test_register_correctly_with_data_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.post(self.create_inventory_url,
                                   self.inventory_data,
                                   HTTP_AUTHORIZATION=auth)
            self.assertEqual(res.status_code, 201)

    # # test to get 1 existing warehouse
    def test_get_one_existing_warehouse_no_token(self):
        self.warehouse_dummy = Warehouse(
            description='testing 1 object retrieval')
        self.warehouse_dummy.save()
        res = self.client.get(
            self.get_warehouse_list_url+"/"+str(self.warehouse_dummy.id)
        )
        self.assertEqual(res.status_code, 401)

    def test_get_one_existing_warehouse_success_token(self):
        self.warehouse_dummy = Warehouse(
                description='testing 1 object retrieval')
        self.warehouse_dummy.save()
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.get(
                self.get_warehouse_list_url+"/"+str(self.warehouse_dummy.id),
                HTTP_AUTHORIZATION=auth
            )
            self.assertEqual(res.status_code, 200)

    # test to get 1 non existing warehouse
    def test_fails_to_get_non_existing_warehouse_no_token(self):
        res = self.client.get(
            self.get_warehouse_list_url+"/"+str(random.randint(1, 10)*5356)
            )
        self.assertEqual(res.status_code, 401)

    def test_fails_to_get_non_existing_warehouse_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.get(
                self.get_warehouse_list_url+"/"+str(random.randint(1, 10)*535),
                HTTP_AUTHORIZATION=auth
                )
            self.assertEqual(res.status_code, 404)

    # test to get 1 existing inventory
    def test_get_one_existing_inventory(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux2 = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux2['token'])
            res_create = self.client.post(
                self.create_inventory_url,
                self.inventory_data,
                HTTP_AUTHORIZATION=auth)
            aux = res_create.json()
            if res_create.status_code == 201:
                res = self.client.get(
                    self.get_inventory_list_url+"/"+str(aux['id']),
                    HTTP_AUTHORIZATION=auth
                )
                self.assertEqual(res.status_code, 200)

    # # test to get 1 non existing inventory
    def test_fails_to_get_non_existing_inventory_no_token(self):
        res = self.client.get(
            self.get_inventory_list_url+str(random.randint(1, 10)*5536)
            )
        self.assertEqual(res.status_code, 404)

    def test_fails_to_get_non_existing_inventory_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            res = self.client.get(
                self.get_warehouse_list_url+str(random.randint(1, 10)*5536),
                HTTP_AUTHORIZATION=auth
                )
            self.assertEqual(res.status_code, 404)

    # # test to register a warehouse with wrong data type
    def test_fails_to_register_warehouse_with_larger_data_no_token(self):
        self.dummy_warehouse_data = {
            'description': 'x'*255
            }
        res = self.client.post(
            self.create_warehouse_url,
            self.dummy_warehouse_data
        )
        self.assertEqual(res.status_code, 401)

    def test_fails_to_register_warehouse_with_larger_data_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            self.dummy_warehouse_data = {
                'description': 'x'*255
                }
            res = self.client.post(
                self.create_warehouse_url,
                self.dummy_warehouse_data,
                HTTP_AUTHORIZATION=auth
            )
            self.assertEqual(res.status_code, 400)

    # # test to register an inventory with wrong data type
    def test_fails_to_register_inventory_enourmus_number_type_no_token(self):
        self.dummy_inventory_data = {
            'stock': 10000000*1000000,
            'warehouse': self.warehouse_dummy.id
        }
        res = self.client.post(
            self.create_inventory_url,
            self.dummy_inventory_data
        )
        self.assertEqual(res.status_code, 401)

    def test_fails_to_register_inventory_enourmus_number_type_sc_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            self.dummy_inventory_data = {
                'stock': 10000000*1000000,
                'warehouse': self.warehouse_dummy.id
            }
            res = self.client.post(
                self.create_inventory_url,
                self.dummy_inventory_data,
                HTTP_AUTHORIZATION=auth
            )
            self.assertEqual(res.status_code, 400)

    # # test to try to register an inventory with wrong stock data type
    def test_fails_to_register_inventory_with_wrong_type_no_token(self):
        self.wrong_inventory_data = {
            'stock': 'test_string',
            'warehouse': self.warehouse_dummy.id
        }
        res = self.client.post(
            self.create_inventory_url,
            self.wrong_inventory_data
        )
        self.assertEqual(res.status_code, 401)

    def test_fails_to_register_inventory_with_wrong_type_succ_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            self.wrong_inventory_data = {
                'stock': 'test_string',
                'warehouse': self.warehouse_dummy.id
            }
            res = self.client.post(
                self.create_inventory_url,
                self.wrong_inventory_data,
                HTTP_AUTHORIZATION=auth
            )
            self.assertEqual(res.status_code, 400)

    # # test to try to register an inventory with a non existing foreign key
    def test_fails_register_inventory_not_foreign_key_no_token(self):
        self.false_inventory_data = {
            'stock': 3000.00,
        }
        res = self.client.post(
            self.create_inventory_url,
            self.false_inventory_data
        )
        self.assertEqual(res.status_code, 401)

    def test_fails_register_inventory_not_foreign_key_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            self.false_inventory_data = {
                'stock': 3000.00,
            }
            res = self.client.post(
                self.create_inventory_url,
                self.false_inventory_data,
                HTTP_AUTHORIZATION=auth
            )
            self.assertEqual(res.status_code, 400)

    def test_fails_register_inventory_false_foreign_key_success_token(self):
        res_auth = self.client.post(self.get_auth_url, self.user_data)
        aux = res_auth.json()
        if(res_auth.status_code == 200):
            auth = 'Bearer {0}'.format(aux['token'])
            self.false_w_inventory_data = {
                'stock': 3000.00,
                'warehouse': 20
            }
            res = self.client.post(
                self.create_inventory_url,
                self.false_w_inventory_data,
                HTTP_AUTHORIZATION=auth
            )
            self.assertEqual(res.status_code, 400)

    def tearDown(self):
        self.usuario.delete()
        self.warehouse_dummy.delete()
        self.usuario_dummy.delete()
