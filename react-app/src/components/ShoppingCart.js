import React from 'react';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';

const ShoppingCart = (props) => {
    const cart = useSelector(state => state.cart)

    return (
        <IconButton>
            <Badge badgeContent={Object.keys(cart).length}>
                <ShoppingCartIcon />
            </Badge>
        </IconButton>
    );
}

export default ShoppingCart;
