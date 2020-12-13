export const AUTHENTICATE_USER = 'AUTHENTICATE_USER';
export const LOGOUT_USER = 'LOGOUT_USER';

export const authAction = user => ({ type: AUTHENTICATE_USER, user });
export const logoutAction = () => ({ type: LOGOUT_USER });

import { clearFavorites, setFavoritesThunk } from './favorites';
import { setProductsThunk } from './products';
import { setCategoriesThunk } from './categories';
import { getAllReviewsThunk } from './reviews';

export const authenticate = () => async dispatch => {
  let user = await fetch('/api/auth/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (user.ok) {
    user = await response.json();
    await dispatch(authAction(data));
    await dispatch(setFavoritesThunk(user.id));
  }
}

export const login = async (email, password) => {
  let user = await fetch('/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email,
      password
    })
  });
  if (user.ok) {
    user = await user.json();
    await dispatch(authAction(user));
    await dispatch(setFavoritesThunk(user.id));
  }
}

export const logout = () => async dispatch => {
  const response = await fetch("/api/auth/logout", {
    headers: {
      "Content-Type": "application/json",
    }
  });
  if (response.ok) {
    const data = await response.json();
    await dispatch(logoutAction());
    await dispatch(clearFavorites());
  }
};


export const signUp = async (username, email, password) => {
  let user = await fetch("/api/auth/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  });
  if (user.ok) {
    user = await user.json();
    await dispatch(authAction(user));
  }
}

export const unauthenticatedUserInfo = () => async dispatch => {
  await dispatch(setCategoriesThunk());
  await dispatch(setProductsThunk());
  await dispatch(getAllReviewsThunk());
}
