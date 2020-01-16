import React from 'react';
import styled from 'styled-components';
import Responsive from '../common/Responsive';
import SubInfo from '../common/SubInfo';
import Tags from '../common/Tags';
import { Link } from 'react-router-dom';
import GridList from '@material-ui/core/GridList';

const PostListBlock = styled(Responsive)`
  margin-top: 3rem;
`;

const PostItemBlock = styled.div`
  background-color: #fafafa;
  margin: 10px;
  padding: 10px;
  width: 275px;
  height: 400px;
  box-shadow: 2px 2px 2px 2px gray;
`;

const PostItem = ({ post }) => {
  const { publishedDate, user, url, tags, title, body, _id } = post;
  return (
    <PostItemBlock>
      <h1>
        <Link to={`/@${user.username}/${_id}`}>{title}</Link>
      </h1>
      <SubInfo
        username={user.username}
        publishedDate={new Date(publishedDate)}
      />
      <img src={url} width="150px" />
      <Tags tags={tags} />
      <h2>{body}</h2>
    </PostItemBlock>
  );
};

const PostList = ({ posts, loading, error, showWriteButton }) => {
  if (error) {
    return <PostListBlock>에러가 발생했습니다.</PostListBlock>;
  }
  return (
    <>
      {!loading && posts && (
        <GridList>
          {posts.map(post => (
            <PostItem post={post} key={post._id} />
          ))}
        </GridList>
      )}
    </>
  );
};

export default PostList;
