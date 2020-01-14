import React, { useState, useRef } from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";

import RecipeReviewCard from "./Card";
import { Grid, GridList } from "@material-ui/core";
import Button from "@material-ui/core/Button";

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`scrollable-auto-tabpanel-${index}`}
      aria-labelledby={`scrollable-auto-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={3}>{children}</Box>}
    </Typography>
  );
}

function a11yProps(index) {
  return {
    id: `scrollable-auto-tab-${index}`,
    "aria-controls": `scrollable-auto-tabpanel-${index}`
  };
}

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    width: "100%",
    backgroundColor: theme.palette.background.paper
  }
}));

export default function ScrollableTabsButtonAuto({ Irin }) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  // const url = `https://i.pinimg.com/originals/d1/1e/c3/d11ec374c68f527bec9a5719e7043fe8.jpg`;
  const [CardArray, setCardArray] = useState([
    <RecipeReviewCard
      id={1}
      url="https://i.pinimg.com/originals/d1/1e/c3/d11ec374c68f527bec9a5719e7043fe8.jpg"
    />,
    <RecipeReviewCard
      id={2}
      url="https://i.pinimg.com/originals/d1/1e/c3/d11ec374c68f527bec9a5719e7043fe8.jpg"
    />,
    <RecipeReviewCard
      id={3}
      url="https://i.pinimg.com/originals/d1/1e/c3/d11ec374c68f527bec9a5719e7043fe8.jpg"
    />,
    <RecipeReviewCard
      id={4}
      url="https://i.pinimg.com/originals/d1/1e/c3/d11ec374c68f527bec9a5719e7043fe8.jpg"
    />,
    <RecipeReviewCard
      id={4}
      url="https://i.pinimg.com/originals/d1/1e/c3/d11ec374c68f527bec9a5719e7043fe8.jpg"
    />
  ]);
  const [CardTwo, setCardTwo] = useState([]);
  const Count = useRef(5);
  const onClick = () => {
    if (Count.current < 7 && Count.current >= 0) {
      setCardArray(
        CardArray.concat(
          <RecipeReviewCard
            id={Count.currnet}
            url="https://i.pinimg.com/originals/d1/1e/c3/d11ec374c68f527bec9a5719e7043fe8.jpg"
          />
        )
      );
    } else {
      setCardTwo(
        CardTwo.concat(
          <RecipeReviewCard
            id={Count.currnet}
            url="https://pbs.twimg.com/media/EKmYbyYU4AAPCZx.jpg"
          />
        )
      );
    }

    Count.current += 1;
  };

  return (
    <div className={classes.root}>
      <Button variant="contained" color="primary" onClick={onClick}>
        +
      </Button>
      <AppBar position="static" color="default">
        <Tabs
          value={value}
          onChange={handleChange}
          indicatorColor="primary"
          textColor="primary"
          variant="scrollable"
          scrollButtons="auto"
          aria-label="scrollable auto tabs example"
        >
          <Tab label="One" {...a11yProps(0)} />
          <Tab label="Two" {...a11yProps(1)} />
          <Tab label="Three" {...a11yProps(2)} />
          <Tab label="Four" {...a11yProps(3)} />
          <Tab label="Five" {...a11yProps(4)} />
        </Tabs>
      </AppBar>
      <TabPanel value={value} index={0}>
        <GridList>{CardArray}</GridList>
      </TabPanel>
      <TabPanel value={value} index={1}>
        <GridList>{CardTwo}</GridList>
      </TabPanel>
      <TabPanel value={value} index={2}>
        Item Three
      </TabPanel>
      <TabPanel value={value} index={3}>
        Item Four
      </TabPanel>
      <TabPanel value={value} index={4}>
        Item Five
      </TabPanel>
      <TabPanel value={value} index={5}>
        Item Six
      </TabPanel>
      <TabPanel value={value} index={6}>
        Item Seven
      </TabPanel>
    </div>
  );
}
