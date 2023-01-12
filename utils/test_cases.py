def test_cases(number):
    return testCases[number]


testCases = [
    ['TEST_01_HomePage_TEST#01', 'when user goes to home page, page should be loaded'],#..0
    ['TEST_02_HomePage_TEST#02', 'In Home page, when user search "Tiger" , User should see result for "Tiger Shark" '],#..1
    ['TEST_03_HomePage_TEST#03', 'In Home page, when user click on any category , User should be navigated to Categorys page '],#..2
    ['TEST_04_HomePage_TEST#04', 'In Home page, when user click on "Cart" Icon , User should be navigated to Shopping Cart page '],#..3
    ['TEST_05_HomePage_TEST#04', 'In Home page, when user click "Sing in" button, he should see Sign in Page'],#.4
    ['TEST_06_LogIn_TEST#01', 'In Login Page, On submitting empty form , User will should get a message "please enter your username and password" '],#..5
    ['TEST_07_LogIn_TEST#02', 'In Login Page, when user login with a valid user, he should see Home Page'],#..6
    ['TEST_09_LogIn_TEST#03', 'In Login Page, when user login with a in-valid user, he should see Error Message'],#..7
    ['TEST_10_LogIn_TEST#04', 'In Login page, when user click "Register" button, he should see Sign up Page'],#..8
    ['TEST_11_SIGNUP_TEST#01', 'In SignUp Page, when user Submit Empty Form He/She should see a Validation" '],#..5
    ['TEST_12_SIGNUP_TEST#02', 'In SignUp Page, If user submits form with wrong userId there should be a validation'],#..6
    ['TEST_13_SIGNUP_TEST#03', 'In SignUp Page, if password and repeated password do not match then form should not be submitted'],#..7
    ['TEST_14_SIGNUP_TEST#04', 'In SignUp page, If user insert wrong email then form should not be submitted'],#..8
    ['TEST_15_SIGNUP_TEST#05', 'In SignUp page, If user insert Incorrect phoneNumber then form should not be submitted'],#..9
    ['TEST_16_SIGNUP_TEST#06', 'In SignUp page, If user do not insert userId then form will not be submitted'],#..10
    ['TEST_17_SIGNUP_TEST#07', 'In SignUp page, If user provides all the required data then form will be submitted'],#..11    
    ['TEST_18_Cart_TEST#01', 'On HomePage, Clicking on Cart Icon should load Up cart Page and Cart Table'],#..16
    ['TEST_19_Cart_TEST#02', 'In Shopping Cart Page, If there is nothing added in the cart, Sub Total should be $0.00'],#..17
    ['TEST_20_Cart_TEST#03', 'In Shopping Cart Page, After adding product to cart should calculate subtotal as per the amount of product'],#..18
    ['TEST_21_Cart_TEST#04', 'In Shopping Cart Page, After removing all product subtotal should be $0.00 and cart should be empty'],#..19
    ['TEST_22_Cart_TEST#05', 'In Shopping Cart Page, Proceed to checkout should navigate to loggin page if not loggedin'],#..20
    ['TEST_23_Cart_TEST#06', 'In Shopping Cart Page, Proceed to checkout should navigate to loggin page if not loggedin and after logging in should be redirected to order confirmation'],#..21
    ['TEST_24_Cart_TEST#07', 'Logged in user should smoothly add product to cart , proceed to check out and recieve order receipt'],#..22
    ['TEST_25_Cart_TEST#02', 'In Shopping Cart Page, Cart Should be empty for first User'],#..23
    ['TEST_26_Update_Acoount_Info_TEST#07', 'when user clicks on the My-_account button it should navigate to update form'],#..24
    ['TEST_27_Update_Acoount_Info_TEST#07', 'when user update password then user should be able to login with the update password'],#..25
]
