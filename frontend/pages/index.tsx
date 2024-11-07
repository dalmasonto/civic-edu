import { Stack, useMantineTheme } from '@mantine/core';
import HeaderAndFooterWrapper from '@/layouts/HeaderAndFooterWrapper';
import Head from 'next/head';
import { APP_NAME } from '@/config/constants';
import Hero from '@/components/pages/Hero';

interface IHomePage {
  faqs?: any
  reviews?: any
  articles?: any
  newsletters?: any[]
}

function HomePage(props: IHomePage) {
  const { faqs, reviews, articles, newsletters } = props
  const theme = useMantineTheme()

  return (
    <>
      <Head>
        <title>{`${APP_NAME} - Home`}</title>
      </Head>
      <Hero />
      <Stack>
      </Stack>
    </>
  );
}


export async function getServerSideProps(context: any) {
  // requireAuthMiddleware(context.req, context.res, () => { })
  // const cookies = context.req.cookies
  // const userDetails_: any = cookies[LOCAL_STORAGE_KEYS.user]

  // const token = cookies[LOCAL_STORAGE_KEYS.token]

  // const userDetails: any = JSON.parse(userDetails_ ?? "{}")

  try {


    return {
      props: {

      }
    }
  } catch (err) {
    return {
      props: {

      }
    }
  }
}

HomePage.PageLayout = HeaderAndFooterWrapper

export default HomePage

