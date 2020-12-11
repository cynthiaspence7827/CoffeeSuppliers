import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import AdminDash from './components/AdminDash';
import Cart from './components/Cart';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import Profile from './components/Profile';
import Home from './components/Home';
import { authenticate } from './store/actions/auth';

function App() {
  const authenticated = useSelector(state => !!state.user);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(authenticate());
  }, [dispatch]);

  return (
    <BrowserRouter>
      <Navbar />
      <Switch>
        <Route path='/' component={<Home />} />
        <Route path='/cart' component={<Cart />} />
        <Route path='/profile' component={<Profile />} />
        <Route path='/admin' component={<AdminDash />} />
      </Switch>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
