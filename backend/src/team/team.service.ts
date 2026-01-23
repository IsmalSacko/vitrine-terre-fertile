import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Team } from './team.entity';

@Injectable()
export class TeamService {

    constructor(
        @InjectRepository(Team)
        private repo: Repository<Team>,
    ) { }

    findAll(): Promise<Team[]> {
        return this.repo.find();
    }

    create(data: Partial<Team>, photo?: string): Promise<Team> {
        const teamMember = this.repo.create({ ...data, photo });
        return this.repo.save(teamMember)
    }

    async updateTeam(id: number, data: Partial<Team>): Promise<Team> {
        const member = await this.repo.preload({ id, ...data });
        if (!member) {
            throw new Error("Ce membre de l'équipe n'existe pas");
        }
        return await this.repo.save(member);
    }

    async updatePhoto(id: number, photo: string): Promise<Team> {
        const member = await this.repo.findOneBy({ id });
        if (!member) {
            throw new Error("Ce membre de l'équipe n'existe pas");
        }
        member.photo = photo;
        return await this.repo.save(member);
    }
    async deleteTeam(id: number): Promise<void> {
        await this.repo.delete(id);
    }


}
