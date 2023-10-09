// import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import AdminDashboard from './AdminDashboard';
import UserDashboard from './UserDashboard';
import PageNotFound from './404';


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      {/* <Route path="/" element={<Home />} /> */}
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/user-dashboard" element={<UserDashboard />} />
      <Route path="/admin-dashboard" element={<AdminDashboard />} />
      <Route path="/page_not_found" element={<PageNotFound />} />
    </Route>
  )
)

function App() {
  return (
    // <Router>
    //   <Switch>
    //     <Route path="/login" component={Login} />
    //     <Route path="/register" component={Register} />
    //     <Route path="/user-dashboard" component={UserDashboard} />
    //     <Route path="/admin-dashboard" component={AdminDashboard} />
    //     <Route path="/page_not_found" component={PageNotFound} />
    //   </Switch>
    // </Router>

    <RouterProvider router={router} />
  )
}

export default App
