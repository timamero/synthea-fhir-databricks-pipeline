import '@mantine/core/styles.css';

import { MantineProvider } from '@mantine/core';
import { Title } from '@mantine/core';

export default function App() {
  return (
    <MantineProvider>
      <div>
        <Title>Synthea FHIR Pipeline</Title>
      </div>
    </MantineProvider>
  );
}
