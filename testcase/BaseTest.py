import pytest
import faker
@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:

    def fake_email(self):
        f = faker.Faker()
        return f.email()
