import React from 'react';
import { useDispatch } from 'react-redux';
import { Card, CardActionArea, CardMedia, CardContent, Typography, Chip } from '@material-ui/core';
import Rating from '@material-ui/lab/Rating';
import { makeStyles } from '@material-ui/core/styles';
import { NavLink } from 'react-router-dom';
import { setCurrentProduct } from '../store/actions/ui';

const useStyles = makeStyles({
    root: {
        maxWidth: 345
    },
    nameAndPrice: {
        display: 'flex',
        justifyContent: 'space-between'
    },
    catChip: {
        margin: '0.5em 0.5em 0 0'
    }
})

const ProductCard = (props) => {
    const classes = useStyles();
    const ui = useSelector(state => state.ui);
    const products = useSelector(state => state.products.dict);
    const categories = useSelector(state => state.categories.dict);
    const dispatch = useDispatch();

    const handleClick = e => {
        dispatch(setCurrentProduct(props.product.id));
    }

    return (
        <Card onClick={handleClick} className={classes.root} component={NavLink} to={`/products/${props.product.id}`}>
            <CardActionArea>
                <CardMedia
                    component="img"
                    alt={props.product.name}
                    image={props.product.images[0]}
                    title={props.product.name}
                />
                <CardContent>
                    <div className={classes.nameAndPrice}>
                        <Typography gutterBottom variant="h5" component="h2">
                            {props.product.name}
                        </Typography>
                        <Typography color='textSecondary' variant="h6" component="h3">
                            {`${props.product.price.toFixed(2)}`}
                        </Typography>
                    </div>
                    <div>
                        {props.product.categories.map(cat => (
                            <Chip className={classes.catChip} label={cat.name} key={`category-${cat.id}`} />
                        ))}
                    </div>
                    <Rating precision={0.1} value={props.product.reviews.reduce((acc, el) => acc + el.rating) / props.product.reviews.length} readOnly />
                </CardContent>
            </CardActionArea>
        </Card>
    );
}

export default ProductCard;
