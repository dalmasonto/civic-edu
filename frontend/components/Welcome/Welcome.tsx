import { Title, Text } from '@mantine/core';
import classes from './Welcome.module.css';

export function Welcome() {
  return (
    <>
      <Title className={classes.title} ta="center" my={50}>
        Welcome to{' '}
        <Text inherit variant="gradient" component="span" gradient={{ from: 'green', to: 'teal' }}>
          Kiboko Dao
        </Text>
      </Title>
    </>
  );
}
