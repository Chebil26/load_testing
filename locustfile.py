from locust import task, between, HttpUser
from OdooLocust.OdooLocustUser import OdooLocustUser

class Seller(OdooLocustUser):
    wait_time = between(0.1, 10)
    host = 'localhost'
    port = 8071
    database="odoo"
    login = "admin"
    password="admin"
    @task(10)
    def read_partners(self):
        customer_model = self.client.get_model('res.partner')
        customer_ids = customer_model.search([])
        customers = customer_model.read(customer_ids)
    @task(5)
    def read_products(self):
        product_model = self.client.get_model('product.product')
        ids = product_model.search([])
        products = product_model.read(ids)
        
class SFA(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_find_one(self):
        self.client.get("api/equipment/identify?equipment_ref=455",
                        headers={"acces-token": "access_token_2bc68191f751b2a36fa5be5a704578f29469b2bc",
                                 'Content-Type': 'application/json'
                                 })