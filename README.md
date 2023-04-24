Simplicity: Writing queries in Python may not be as clear as writing in SQL, but it’s less error-prone and more efficient, as you don’t have to control which type of database you are working with before trying to understand the code.
Consistency: SQL is inconsistent across different databases. Working with Django models creates an abstraction and helps you focus on the most important tasks.
Tracking: It’s even easier to track database design changes working with Django models. It’s done by reading migration files written in Python. We’ll discuss this more in the next chapter.

However, when Django is coupled with DRF, the model can be directly connected to the view. However, as good practice, use a serializer between a model and a viewset. This really helps with validation and also some important checks.

a package that will handle JWT authentication for us. The djangorestframework-simplejwt package is a JWT authentication plugin for DRF:
pip install djangorestframework-simplejwt

One-to-one: In this type of relationship, a row in table A can only have one matching row in table B, and vice versa. An example of this can be worker C having one and only one desk D. And this desk D can only be used by this worker C 

Many-to-many: In this type of database relationship, a row in table A can have many matching rows in table B, and vice versa. For example, in an e-commerce application, an order can have many items, and an item can also appear in many different orders (Figure 3.4):

If authentication is the action of verifying the identity of a user, authorization is simply the action of checking whether the user has the rights or privileges to perform an action.

Pytest, taken alone, is simply a Python framework to write unit tests in Python programs.
pip install pytest-django

JSX styling
JSX is a syntax extension to JavaScript that allows you to write JavaScript code that looks like HTML. It was introduced by Facebook as part of the React library, but it can be used with other JavaScript libraries and frameworks as well. Here is an example of how you might use JSX in a React component:

The Context API is a way to share data between different components in a React application. It allows you to pass data through the component tree without having to pass props down manually at every level. Here is an example of how you might use the Context API in a React application:

`// Create a context for sharing data
const Context = React.createContext();
function App() {
  // Set some initial data in the context
  const data = {
    message: 'Hello, world!'
  };
  return (
    // Provide the data to the components inside the
    // Provider
    <Context.Provider value={data}>
      <Component />
    </Context.Provider>
  );
}
function Component() {
  // Use the useContext Hook to access the data in the
  // context
  const context = React.useContext(Context);
  return (
    <p>{context.message}</p>
  );
}

useMemo
useMemo is a Hook in React that allows you to optimize the performance of your components by memoizing expensive calculations. It works by returning a memoized value that is only recalculated if one of the inputs to the calculation changes.

Important note

Memoization is a technique used in computer programming to speed up programs by storing the results of expensive function calls and returning the cached result when the same inputs are given again. This can be useful for optimizing programs that make many repeated calculat

`
Handling forms – controlled components and uncontrolled components
A controlled component is a component in React that is controlled by the state of the parent component. This means that the value of the input field is determined by the value prop passed to the component, and any changes to the input are handled by the parent component.

On the other hand, an uncontrolled component is a component in React that manages its own state internally. This means that the value of the input field is determined by the defaultValue prop passed to the component, and any changes to the input are handled by the component itself.

An access token with a lifetime of 5 minutes: This token helps with authenticating on the server side when requesting without the need to log in again. Then, we can access resources and perform actions on these resources.
A refresh token: This token helps you to retrieve another access token if one has already expired.

With this data coming from the server, we can manage authentication from the React application side like so. When a registration or a login is successful, we store the returned response in the client’s browser; we’ll use localStorage for this.

The localStorage property helps us to work with the browser storage, enabling browsers to store key-value pairs in the browser. Two methods will be used with localStorage: setItem() to set a key-value pair and getItem() to access the values.

he Authorization header to the request containing the access token retrieved from localStorage. If the request returns a 401 error, it means that the token has expired. If this happens, we send a request to the refresh endpoint to get a new access token, using the refresh token also retrieved from localStorage. And with this access token, we resend the failed request.

If we receive a 401 error again, it means that the refresh token has expired. Then, the user will be sent to the login page to log in again, retrieve new tokens, and store them in localStorage.

Now that we understand the authentication flow from the frontend side, let’s write the requests service we will use for data fetching and performing CRUD actions.

axios package for HTTP requests.
Axios is a popular library mainly used to send asynchronous HTTP requests to REST endpoints.
However, we will also install axios-auth-refresh. This simple library assists with an automatic refresh of tokens via axios interceptors. To install the axios and axios-auth-refresh packages, follow these steps:


Instead of repeating the same code across the code base, we can follow the Don’t Repeat Yourself (DRY) rule.

We can now add the login and logout functions. These functions will return Promise, which, if successful, will register the user data in localStorage and redirect the user to the home page, or allow us to catch and handle errors.

Writing functions in JavaScript using the function keyword allows hoisting, meaning that functions declaration is moved to the top of their scope before code execution.

Host
ec2-52-215-68-14.eu-west-1.compute.amazonaws.com
Database
d17t717sc0cgrr
User
mcfanfhaxvtswv
Port
5432
Password
3c50b2ef08268f38bc83d100135b0f1017d1fb25bd156bb62808c960761d318c