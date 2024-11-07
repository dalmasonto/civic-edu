import { Box, Center, Container, Grid, Image, Stack, Title } from '@mantine/core'
import React from 'react'

const Hero = () => {
    return (
        <Container fluid py={'50px'} bg={'rgba(0, 0, 0, 0.1)'}>
            <Grid>
                <Grid.Col span={{ md: 6 }}>
                    <Stack py={'30py'} h={'450px'} justify='center'>
                        <Title size={'52px'}>Keep Learning <br /> On Track</Title>
                    </Stack>
                </Grid.Col>
                <Grid.Col span={{ md: 6 }}>
                    <Image src={'/assets/images/hero.png'} h={'450px'} mx={'auto'} w={'auto'} />
                </Grid.Col>
            </Grid>
        </Container>
    )
}

export default Hero