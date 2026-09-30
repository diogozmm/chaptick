import { ItemType } from '../core/content/content.models';
import { IconName } from './icon/icons';

/** Each type has an icon and a color token (--type-<type>), so it is never told apart by color alone. */
export const TYPE_ICON: Record<ItemType, IconName> = {
  quest: 'scroll-text',
  hidden_quest: 'eye-off',
  missable: 'hourglass',
  collectible: 'gem',
};
