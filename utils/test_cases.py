def test_cases(number):
    return testCases[number]


testCases = [
    ['Blocker', 'when user goes to home page, page should be loaded'],#..
    ['Blocker', 'In Home page, when user search "Tiger" , User should see result for "Tiger Shark" '],#..
    ['Blocker', 'In Home page, when user click on any category , User should be navigated to Categorys page '],#..
    ['Blocker', 'In Login Page, On submitting empty form , User will should get a message "please enter your username and password" '],#..
    ['Blocker', 'In Home page, when user click "Sing in" button, he should see Sign in Page'],
    ['Blocker', 'In Login page, when user click "Register" button, he should see Sign up Page'],
    ['Blocker', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['Blocker', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
    ['Blocker', 'In Shopping Cart Page, If there is nothing added in the cart, Sub Total should be $0.00'],
]
