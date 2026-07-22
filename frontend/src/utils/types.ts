export interface ConditionCountsResponse {
  gender: string;
  condition_description: string;
  condition_count: number;
}

export interface PivotedConditionCounts {
  condition_description: string;
  male?: number;
  female?: number;
}
