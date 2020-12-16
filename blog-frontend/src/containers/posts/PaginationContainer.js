import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import PersonPinIcon from '@material-ui/icons/PersonPin';
import HelpIcon from '@material-ui/icons/Help';
import ShoppingBasket from '@material-ui/icons/ShoppingBasket';
import ThumbDown from '@material-ui/icons/ThumbDown';
import ThumbUp from '@material-ui/icons/ThumbUp';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import qs from 'querystring';
import { Link } from 'react-router-dom';
function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`scrollable-force-tabpanel-${index}`}
      aria-labelledby={`scrollable-force-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={3}>{children}</Box>}
    </Typography>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `scrollable-force-tab-${index}`,
    'aria-controls': `scrollable-force-tabpanel-${index}`,
  };
}

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    width: '100%',
    backgroundColor: theme.palette.background.paper,
  },
}));

const buildLink = ({ username, tag, page }) => {
  const query = qs.stringify({ tag, page });
  return username ? `/@${username}?${query}` : `/?${query}`;
};

export default function ScrollableTabsButtonForce({ username, tag, page }) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <AppBar position="static" color="default">
        <Tabs
          value={value}
          onChange={handleChange}
          variant="scrollable"
          scrollButtons="on"
          indicatorColor="primary"
          textColor="primary"
          aria-label="scrollable force tabs example"
        >
          <Link to={buildLink({ username, tag, page: 1 })}>
            <Tab label="PAGE1" icon={<PersonPinIcon />} {...a11yProps(1)} />
          </Link>
          <Link to={buildLink({ username, tag, page: 2 })}>
            <Tab label="PAGE2" icon={<PersonPinIcon />} {...a11yProps(2)} />
          </Link>
          <Link to={buildLink({ username, tag, page: 3 })}>
            <Tab label="PAGE3" icon={<HelpIcon />} {...a11yProps(3)} />
          </Link>
          <Link to={buildLink({ username, tag, page: 4 })}>
            <Tab label="PAGE4" icon={<ShoppingBasket />} {...a11yProps(4)} />
          </Link>
          <Link to={buildLink({ username, tag, page: 5 })}>
            <Tab label="PAGE5" icon={<ThumbDown />} {...a11yProps(5)} />
          </Link>
          <Link to={buildLink({ username, tag, page: 6 })}>
            <Tab label="PAGE6" icon={<ThumbUp />} {...a11yProps(6)} />
          </Link>
        </Tabs>
      </AppBar>
    </div>
  );
}
