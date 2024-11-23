from locust import task, between, HttpUser
# from OdooLocust.OdooLocustUser import OdooLocustUser

# class Seller(OdooLocustUser):
#     wait_time = between(0.1, 10)
#     host = 'localhost'
#     port = 8071
#     database="odoo"
#     login = "admin"
#     password="admin"
#     @task(10)
#     def read_partners(self):
#         customer_model = self.client.get_model('res.partner')
#         customer_ids = customer_model.search([])
#         customers = customer_model.read(customer_ids)
#     @task(5)
#     def read_products(self):
#         product_model = self.client.get_model('product.product')
#         ids = product_model.search([])
#         products = product_model.read(ids)
        
class PresalioHttpUser(HttpUser):
    abstract = True

    def _get_default_header(self):
        return {"Content-Type": "application/json"}

    def autenticate_supervisor(self):
        self.client.post("api/user/authenticate",
                                json={
                                    "login": "REG01",
                                    "password": "aa",
                                    "db": "odoo"
                                },
                                headers=self._get_default_header())
    


class SFA(PresalioHttpUser):
    wait_time = between(1, 2)

    @task
    def test_find_one(self):
        self.client.get("api/equipment/identify?equipment_ref=455",
                        headers=self._get_default_header())
                            

class SupervisorStockSnapshot(PresalioHttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.autenticate_supervisor()

    @task
    def stock_snapshot(self):
        res = self.client.post("api/stock/snapshot/31cf7083-f222-4e41-b2f0-688b0f71d39a",
                        headers=self._get_default_header())
        # print(res)

                
class SupervisorWorkflow(PresalioHttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.autenticate_supervisor()


    # @task
    # def stock_snapshot(self):
    #     res = self.client.post("api/stock/snapshot/31cf7083-f222-4e41-b2f0-688b0f71d39a",
    #                     headers=self._get_default_header())
    #     # print(res)

    @task
    def get_user_list(self):
        res = self.client.get("api/supervisor/user",
                        headers=self._get_default_header())
        print(res)
    @task
    def get_user_position(self):
        res = self.client.get("api/supervisor/position",
                        headers=self._get_default_header())
        print(res)
                
    @task
    def get_user_detail(self):
        res = self.client.get("api/supervisor/user/720ff356-2d91-49fe-9680-0152b99057df",
                        headers=self._get_default_header())
        print(res)
                
    @task
    def get_pos_list(self):
        res = self.client.get("api/supervisor/user/720ff356-2d91-49fe-9680-0152b99057df/visit",
                        headers=self._get_default_header())
        print(res)

    @task
    def get_user_visit_history(self):
        res = self.client.get("api/supervisor/user/720ff356-2d91-49fe-9680-0152b99057df/history",
                        headers=self._get_default_header())
        print(res)

    @task
    def get_user_visits_info(self):
        res = self.client.get("api/supervisor/user/6830c6b6-6c92-4a87-b516-a734ae943270/stats/visits",
                        headers=self._get_default_header())

        print(res)
