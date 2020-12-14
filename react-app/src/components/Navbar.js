import { Badge, Button, IconButton } from '@material-ui/core';
import React from 'react';
import { useSelector } from 'react-redux';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import DashboardIcon from '@material-ui/icons/Dashboard';
import FavoriteIcon from '@material-ui/icons/Favorite';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';

const Navbar = (props) => {
    const user = useSelector(state => state.user);
    const cart = useSelector(state => state.cart);

    return (
        <div>
            {/* <IconButton startIcon={<ShoppingCartIcon />}>
                Coffee Suppliers
            </IconButton> */}
            <Button>
                <Badge badgeContent={Object.keys(cart).length}>
                    <ShoppingCartIcon />
                </Badge>
            </Button>
            <Button>
                Sign In
            </Button>
            <Button>
                Sign Up
            </Button>
        </div>
    );
}

export default Navbar;
