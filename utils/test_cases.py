def test_cases(number):
    return testCases[number]


testCases = [
    ['TEST_01_HomePage_TEST#01', 'when user goes to home page, page should be loaded'],#..
    ['TEST_02_HomePage_TEST#02', 'In Home page, when user search "Tiger" , User should see result for "Tiger Shark" '],#..
    ['TEST_03_HomePage_TEST#03', 'In Home page, when user click on any category , User should be navigated to Categorys page '],#..
    ['TEST_05_HomePage_TEST#04', 'In Home page, when user click "Sing in" button, he should see Sign in Page'],
    ['TEST_04_LogIn_TEST#01', 'In Login Page, On submitting empty form , User will should get a message "please enter your username and password" '],#..
    ['TEST_06_LogIn_TEST#02', 'In Login page, when user click "Register" button, he should see Sign up Page'],
    ['TEST_07_LogIn_TEST#03', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['TEST_08_LogIn_TEST#04', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
    ['TEST_09', 'In Shopping Cart Page, If there is nothing added in the cart, Sub Total should be $0.00'],
]
