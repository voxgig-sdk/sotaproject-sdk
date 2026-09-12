import { SotaprojectEntityBase } from '../SotaprojectEntityBase';
import type { SotaprojectSDK } from '../SotaprojectSDK';
import type { Control } from '../types';
import type { Publication, PublicationListMatch } from '../SotaprojectTypes';
declare class PublicationEntity extends SotaprojectEntityBase<Publication> {
    constructor(client: SotaprojectSDK, entopts: any);
    make(this: PublicationEntity): PublicationEntity;
    list(this: any, reqmatch?: PublicationListMatch, ctrl?: Control): Promise<PublicationEntity[]>;
}
export { PublicationEntity };
