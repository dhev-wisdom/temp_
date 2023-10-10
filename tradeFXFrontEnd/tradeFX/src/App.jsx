import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom';
import AdminDashboard from './AdminDashboard';
import UserDashboard from './UserDashboard';
import PageNotFound from './404';


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path="/" element={<AdminDashboard />} />
      <Route path="/user-dashboard" element={<UserDashboard />} />
      <Route path="/admin-dashboard" element={<AdminDashboard />} />
      <Route path="/page_not_found" element={<PageNotFound />} />
    </Route>
  )
);

function App() {
  return (
    <RouterProvider router={router} />
  )
}

export default App
