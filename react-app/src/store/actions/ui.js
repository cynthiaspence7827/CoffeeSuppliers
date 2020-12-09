export const SET_CURRENT_PRODUCT = 'SET_CURRENT_PRODUCT';
export const SET_CURRENT_CATEGORY = 'SET_CURRENT_CATEGORY';
export const OPEN_SIGN_IN = 'OPEN_SIGN_IN';
export const OPEN_SIGN_UP = 'OPEN_SIGN_UP';
export const CLOSE_AUTH_DIALOG = 'CLOSE_AUTH_DIALOG';

export const setCurrentProduct = id => ({ type: SET_CURRENT_PRODUCT, id });
export const setCurrentCategory = id => ({ type: SET_CURRENT_CATEGORY, id });
export const openSignIn = () => ({ type: OPEN_SIGN_IN });
export const openSignUp = () => ({ type: OPEN_SIGN_UP });
export const closeAuthDialog = () => ({ type: CLOSE_AUTH_DIALOG });
