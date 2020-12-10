export const ADD_TO_CART = 'ADD_TO_CART';
export const REMOVE_FROM_CART = 'REMOVE_FROM_CART';
export const CLEAR_CART = 'CLEAR_CART';
export const UPDATE_CART_ITEM = 'UPDATE_CART_ITEM';

export const addToCart = product => ({ type: ADD_TO_CART, product });
export const removeFromCart = productId => ({ type: REMOVE_FROM_CART, productId });
export const clearCart = () => ({ type: CLEAR_CART });
export const updateCartItem = updatedItem => ({ type: UPDATE_CART_ITEM, updatedItem });
