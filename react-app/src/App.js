import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { authenticate } from "./store/actions/auth";

function App() {
  const authenticated = useSelector(state => !!state.user);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatchEvent(authenticate());
  }, [dispatch]);

  return (
    <BrowserRouter>
      
      <Switch>
        <Route path='/' >
          {authenticated
            ? <h1>Authenticated</h1>
            : <h1>Not Authenticated</h1>}
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
