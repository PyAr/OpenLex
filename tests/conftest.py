@pytest.fixture
def context(context):
    context.setDefaultTimeout(10000)
    yield context
