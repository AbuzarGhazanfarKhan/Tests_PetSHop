def test_cases(number):
    return testCases[number]


testCases = [
    ['TEST_01', 'when user goes to home page, page should be loaded'],#..
    ['TEST_02', 'In Home page, when user search "Tiger" , User should see result for "Tiger Shark" '],#..
    ['TEST_03', 'In Home page, when user click on any category , User should be navigated to Categorys page '],#..
    ['TEST_04', 'In Login Page, On submitting empty form , User will should get a message "please enter your username and password" '],#..
    ['TEST_05', 'In Home page, when user click "Sing in" button, he should see Sign in Page'],
    ['TEST_06', 'In Login page, when user click "Register" button, he should see Sign up Page'],
    ['TEST_07', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['TEST_08', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
    ['TEST_09', 'In Shopping Cart Page, If there is nothing added in the cart, Sub Total should be $0.00'],
]
