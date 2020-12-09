export const SET_PRODUCTS = 'SET_PRODUCTS';

export const setProducts = products => ({ type: SET_PRODUCTS, products});

export const setProductsThunk = () => async dispatch => {
    let products = await fetch(`/api/products`);
    if (products.ok) {
        products = await products.json();
        dispatch(setProducts(products));
    }
}
