import { useState, useEffect } from 'react';
import '@mantine/core/styles.css';

import { MantineProvider } from '@mantine/core';
import { Title } from '@mantine/core';

import {
  fetchConditionCounts,
  type ConditionCountsResponse,
} from './services/syntheaApiService';

export default function App() {
  const [conditionCounts, setConditionCounts] = useState<
    ConditionCountsResponse[] | null
  >(null);

  const baseUrl = 'http://localhost:8080';

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchConditionCounts(baseUrl);

      if (data) {
        setConditionCounts(data);
      } else {
        console.warn('No condition counts data received from the API.');
      }
    };

    fetchData();
  }, []);

  console.log('conditionCounts:', conditionCounts);

  return (
    <MantineProvider>
      <div>
        <Title>Synthea FHIR Pipeline</Title>
      </div>
    </MantineProvider>
  );
}
