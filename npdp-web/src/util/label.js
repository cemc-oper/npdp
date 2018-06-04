import * as d3sc from 'd3-scale-chromatic';

export function generateTagColorMap(label_set) {
  let tag_color_map = new Map();
  let step=1.0/(label_set.size + 1);
  let current_value = 0.0;
  label_set.forEach((value) => {
    tag_color_map.set(value, d3sc.interpolateRainbow(current_value));
    current_value+=step;
  });
  return tag_color_map;
}