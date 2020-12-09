import React, { useState, useEffect } from "react";
import { useSelector } from 'react-redux';
import { BrowserRouter, Route, Switch } from "react-router-dom";
// import { authenticate } from "./services/auth";

function App() {
  const authenticated = useSelector(state => !!state.user)
  // const [loaded, setLoaded] = useState(false);

  // useEffect(() => {
  //   (async () => {
  //     const user = await authenticate();
  //     if (!user.errors) {
  //       setAuthenticated(true);
  //     }
  //     setLoaded(true);
  //   })();
  // }, []);

  // if (!loaded) {
  //   return null;
  // }

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
