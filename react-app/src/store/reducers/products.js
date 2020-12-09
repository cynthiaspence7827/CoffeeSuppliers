import { SET_PRODUCTS } from "../actions/products";

const initialState = {
    dict: {},
    ids: []
};

export default function reducer(state = initialState, action) {
    let newState = { ...state };

    switch (action.type) {
        case SET_PRODUCTS:
            newState.dict = action.products.dict;
            newState.ids = action.products.ids;
        default:
            return state;
    }
}
