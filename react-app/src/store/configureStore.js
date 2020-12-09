import { createStore, applyMiddleware, combineReducers, compose } from 'redux';
import thunk from 'redux-thunk';
import user from '../store/reducers/user';
import users from '../store/reducers/users';
import reviews from '../store/reducers/reviews';
import favorites from '../store/reducers/favorites';
import purchases from '../store/reducers/purchases';
import products from '../store/reducers/products';
import categories from '../store/reducers/categories';
import ui from '../store/reducers/ui';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const reducer = combineReducers({
    user,
    users,
    reviews,
    favorites,
    purchases,
    products,
    categories,
    ui
});

const configureStore = (initialState) => {
    return createStore(reducer, initialState, composeEnhancers(applyMiddleware(thunk)));
};

export default configureStore;
