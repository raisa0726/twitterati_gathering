import React from 'react';
import { NextPage, NextPageContext } from 'next';
import styled from 'styled-components';

// production時(next buildの成果物を使っている時)のエラー表示に使われる
// See Also: https://nextjs.org/docs/advanced-features/custom-error-page
const ErrorArea = styled.div`
  font-family:-apple-system, BlinkMacSystemFont, Roboto, "Segoe UI", "Fira Sans", Avenir, "Helvetica Neue", "Lucida Grande", sans-serif;
  position: absolute;
  top: 50vh;
  left: 50vw;
  -webkit-transform : translate(-50%,-50%);
  transform : translate(-50%,-50%);
  text-align: center;
`
const ErrorStatu = styled.h1`
  display:inline-block;
  border-right:1px solid #9090904c;
  margin:0;
  margin-right:20px;
  padding:10px 23px 10px 0;
  font-size:24px;
  font-weight:500;
  vertical-align:top;
`
const ErrorSentence = styled.div`
  display:inline-block;
  text-align:left;
  line-height:49px;
  height:49px;
  vertical-align:middle;
  *{
    display:inline-block;
    text-align:left;
    line-height:49px;
    height:49px;
    vertical-align:middle;
  }
`
interface Props {
  statusCode: number;
}
const Error: NextPage<Props> = ({ statusCode }) => {
  // ここでエラーページをちゃんと構築する。statusCodeが400の時BadRequest、
  // 404/405の時Not Found、500の問Internal Server Errorが出るように正しく処理すれば良いだろう
  return (
    <ErrorArea>
      <ErrorStatu>{statusCode}</ErrorStatu>
      <ErrorSentence>エラーが発生しました</ErrorSentence>
    </ErrorArea>
    )
};

Error.getInitialProps = async ({ res, err }: NextPageContext) => {
  // statusCodeを算出する。
  // - resが存在する時はSSRであり、res.statusCodeをそのまま利用すれば良い。
  // - resがない場合はCSRである。
  //   - err.statusCodeがあればそれをそのまま利用する
  //   - 意図しない例外が起きてerrがここに渡ってくる場合、単なるErrorオブジェクトが入っていてstatusCodeプロパティがない。errがある時点でISEなので500にする
  // See Also: https://nextjs.org/docs/advanced-features/custom-error-page
  const statusCode = res ? res.statusCode : err ? err.statusCode ?? 500 : 404;

  return { statusCode };
};

export default Error;
