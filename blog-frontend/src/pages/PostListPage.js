import React from 'react';
import PostListContainer from '../containers/posts/PostListContainer';
import PaginationContainer from '../containers/posts/PaginationContainer';
import BarChart from '../components/chart/chart';

const PostListPage = () => {
  return (
    <>
      <BarChart />
      <PaginationContainer />
      <PostListContainer />
    </>
  );
};

export default PostListPage;
